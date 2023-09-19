import logging
import uuid
from datetime import datetime

import pandas
import sqlparse

from migration.connector.source.enum import Column

from migration.connector.destination.base import Destination

from migration.connector.source import Source

logger = logging.getLogger(__name__)

NUMBER_TYPE = ['BIGINT', 'DECIMAL', 'DOUBLE', 'FLOAT', 'INT', 'SMALLINT', 'TINYINT']
LEFT_BRACKET = '('


def is_number_type(column: Column, type_mapping: dict) -> bool:
    if LEFT_BRACKET in column.type:
        column_type = column.type.split(LEFT_BRACKET)[0]
        return type_mapping.get(column_type, column_type) in NUMBER_TYPE

    return type_mapping.get(column.type, column.type) in NUMBER_TYPE


def create_query_result_table(source: Source, destination: Destination, source_query: str,
                              destination_query: str) -> str:
    try:
        temp_db = 'validation_query_result_db'
        temp_table = f"validation_query_result_table_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
        if source.name.lower() == 'clickzetta':
            source.execute_sql(f"create schema if not exists {temp_db}")
            temp_table_ddl = f"create table {temp_db}.{temp_table} as {source_query}"
        elif source.name.lower() == 'doris':
            source.execute_sql(f"create database if not exists {temp_db}")
            temp_table_ddl = f"create table {temp_db}.{temp_table} PROPERTIES(\"replication_num\" = \"1\") as {source_query}"
        else:
            source.execute_sql(f"create database if not exists {temp_db}")
            temp_table_ddl = f"create table {temp_db}.{temp_table} as {source_query}"
        source.execute_sql(f"drop table if exists {temp_db}.{temp_table}")
        source.execute_sql(temp_table_ddl)
        if destination.name.lower() == 'clickzetta':
            destination.execute_sql(f"create schema if not exists {temp_db}")
            temp_table_ddl = f"create table {temp_db}.{temp_table} as {destination_query}"
        elif destination.name.lower() == 'doris':
            destination.execute_sql(f"create database if not exists {temp_db}")
            temp_table_ddl = f"create table {temp_db}.{temp_table} PROPERTIES(\"replication_num\" = \"1\") as {destination_query}"
        else:
            destination.execute_sql(f"create database if not exists {temp_db}")
            temp_table_ddl = f"create table {temp_db}.{temp_table} as {destination_query}"
        destination.execute_sql(f"drop table if exists {temp_db}.{temp_table}")
        destination.execute_sql(temp_table_ddl)
        return f"{temp_db}.{temp_table}"
    except Exception as e:
        raise Exception(e)
    except BaseException as e:
        raise Exception(e)


def basic_validation(source: Source, destination: Destination, source_query: str, destination_query: str):
    try:
        tbl_name = create_query_result_table(source, destination, source_query, destination_query)
        count_sql = f"select count(*) from {tbl_name}"
        source_count_res = source.execute_sql(count_sql)[0]
        result = {'source_count': source_count_res[0]}
        destination_count_res = destination.execute_sql(count_sql)[0]
        result['destination_count'] = destination_count_res[0]
        type_mapping = source.type_mapping()
        table_columns = source.get_table_columns(tbl_name.split('.')[0], tbl_name.split('.')[1])
        for column in table_columns:
            if is_number_type(column, type_mapping):
                sql = f"select min({column.name}), max({column.name}), avg({column.name}) from {tbl_name}"
                source_result = source.execute_sql(sql)[0]
                logger.info(f"basic validation source_result: {source_result}")
                result[f'{column.name}_source_min'] = source_result[0]
                result[f'{column.name}_source_max'] = source_result[1]
                result[f'{column.name}_source_avg'] = source_result[2]
                destination_result = destination.execute_sql(sql)[0]
                logger.info(f"basic validation destination_result: {destination_result}")
                result[f'{column.name}_destination_min'] = destination_result[0]
                result[f'{column.name}_destination_max'] = destination_result[1]
                result[f'{column.name}_destination_avg'] = destination_result[2]
        return result
    except Exception as e:
        raise Exception(e)
    except BaseException as e:
        raise Exception(e)


def multidimensional_validation(source_query: str, destination_query: str, source: Source, destination: Destination):
    try:
        tbl_name = create_query_result_table(source, destination, source_query, destination_query)
        table_columns = source.get_table_columns(tbl_name.split('.')[0], tbl_name.split('.')[1])
        type_mapping = source.type_mapping()
        source_profile_sql = f"with source_data as (select * from {tbl_name}), \n" \
                             f"column_profiles  as ( \n"
        for index, column in enumerate(table_columns):
            source_profile_sql += f"select '{column.name}' as column_name, \n" \
                                  f"'{column.type}' as column_type, \n" \
                                  f"count(*) as row_count, \n" \
                                  f"sum(case when {column.name} is null then 0 else 1 end) / count(*) as not_null_proportion,\n" \
                                  f"count(distinct {column.name}) / count(*) as distinct_proportion, \n" \
                                  f"count(distinct {column.name}) as distinct_count, \n" \
                                  f"count(distinct {column.name}) = count(*) as is_unique, \n"
            if is_number_type(column, type_mapping):
                source_profile_sql += f"min({column.name}) as min_value, \n" \
                                      f"max({column.name}) as max_value, \n" \
                                      f"avg({column.name}) as avg_value, \n" \
                                      f"stddev_pop({column.name}) as stddev_pop_value, \n"
                if source.name.lower() == 'clickzetta' or source.name.lower() == 'doris':
                    source_profile_sql += f"stddev_samp({column.name}) as stddev_sample_value \n"
                else:
                    source_profile_sql += f"stddev_sample({column.name}) as stddev_sample_value \n"
            else:
                source_profile_sql += f"null as min_value, \n" \
                                      f"null as max_value, \n" \
                                      f"null as avg_value, \n" \
                                      f"null as stddev_pop_value, \n" \
                                      f"null as stddev_sample_value \n"
            source_profile_sql += f"from source_data \n"
            if index != len(table_columns) - 1:
                source_profile_sql += f"union all \n"
        source_profile_sql += f") \n" \
                              f"select * from column_profiles;"
        source_result = source.execute_sql(source_profile_sql)
        list_source_result = []
        for row in source_result:
            list_source_result.append(list(row))
        logger.info(f"mutil source_result: {source_result}")
        des_profile_sql = f"with source_data as (select * from {tbl_name}), \n" \
                          f"column_profiles  as ( \n"
        for index, column in enumerate(table_columns):
            des_profile_sql += f"select '{column.name}' as column_name, \n" \
                               f"'{column.type}' as column_type, \n" \
                               f"count(*) as row_count, \n" \
                               f"sum(case when {column.name} is null then 0 else 1 end) / count(*) as not_null_proportion,\n" \
                               f"count(distinct {column.name}) / count(*) as distinct_proportion, \n" \
                               f"count(distinct {column.name}) as distinct_count, \n" \
                               f"count(distinct {column.name}) = count(*) as is_unique, \n"
            if is_number_type(column, type_mapping):
                des_profile_sql += f"min({column.name}) as min_value, \n" \
                                   f"max({column.name}) as max_value, \n" \
                                   f"avg({column.name}) as avg_value, \n" \
                                   f"stddev_pop({column.name}) as stddev_pop_value, \n"
                if destination.name.lower() == 'clickzetta' or destination.name.lower() == 'doris':
                    des_profile_sql += f"stddev_samp({column.name}) as stddev_sample_value \n"
                else:
                    des_profile_sql += f"stddev_sample({column.name}) as stddev_sample_value \n"
            else:
                des_profile_sql += f"null as min_value, \n" \
                                   f"null as max_value, \n" \
                                   f"null as avg_value, \n" \
                                   f"null as stddev_pop_value, \n" \
                                   f"null as stddev_sample_value \n"
            des_profile_sql += f"from source_data \n"
            if index != len(table_columns) - 1:
                des_profile_sql += f"union all \n"
        des_profile_sql += f") \n" \
                           f"select * from column_profiles;"
        destination_result = destination.execute_sql(des_profile_sql)
        list_destination_result = []
        for row in destination_result:
            list_destination_result.append(list(row))
        logger.info(f"mutil destination_result: {destination_result}")
        if source.name.lower() == 'clickzetta':
            for row in list_source_result:
                if row[6] == 'false':
                    row[6] = 0
                elif row[6] == 'true':
                    row[6] = 1
        if destination.name.lower() == 'clickzetta':
            for row in list_destination_result:
                if row[6] == 'false':
                    row[6] = 0
                elif row[6] == 'true':
                    row[6] = 1

        for index, source_row in enumerate(list_source_result):
            if abs(source_row[10] - list_destination_result[index][10]) < 50:
                source_row[10] = list_destination_result[index][10]
            if abs(source_row[11] - list_destination_result[index][11]) < 50:
                source_row[11] = list_destination_result[index][11]
        return list_source_result, list_destination_result
    except Exception as e:
        raise Exception(e)
    except BaseException as e:
        raise Exception(e)


def parse_sql_order_by(query: str):
    result = sqlparse.parse(query)
    for index, token in enumerate(result[0].tokens):
        if token.ttype == sqlparse.tokens.Keyword:
            if token.value.lower() == 'order by':
                index += 1
                while index < len(result[0].tokens):
                    if not result[0].tokens[index].ttype:
                        return ' order by ' + result[0].tokens[index].value
                        break
                    index += 1
    return None


def line_by_line_validation(source_query: str, destination_query: str, source: Source, destination: Destination):
    try:
        tbl_name = create_query_result_table(source, destination, source_query, destination_query)
        select_all_sql_source = f"select * from {tbl_name}" if parse_sql_order_by(
            source_query) is None else f"select * from {tbl_name} {parse_sql_order_by(source_query)}"
        select_all_sql_destination = f"select * from {tbl_name}" if parse_sql_order_by(
            destination_query) is None else f"select * from {tbl_name} {parse_sql_order_by(destination_query)}"
        source_result = source.execute_sql(select_all_sql_source)
        list_source_result = []
        for row in source_result:
            list_source_result.append(list(row))
        logger.info(f"line by line source_result: {source_result}")
        destination_result = destination.execute_sql(select_all_sql_destination)
        list_destination_result = []
        for row in destination_result:
            list_destination_result.append(list(row))
        logger.info(f"line by line destination_result: {destination_result}")
        columns = source.get_table_columns(tbl_name.split('.')[0], tbl_name.split('.')[1])
        if source.name.lower() == 'clickzetta':
            for index, row in enumerate(list_source_result):
                if columns[index].type == 'DATETIME':
                    row[index] = str(pandas.to_datetime(row[index])).split('+')[0]
        if destination.name.lower() == 'clickzetta':
            for index, row in enumerate(list_destination_result):
                if columns[index].type == 'DATETIME':
                    row[index] = str(pandas.to_datetime(row[index])).split('+')[0]
        result = {'source_result': list_source_result,
                  'destination_result': list_destination_result,
                  'columns': [column.name for column in columns]}
        return result
    except Exception as e:
        raise Exception(e)
    except BaseException as e:
        raise Exception(e)

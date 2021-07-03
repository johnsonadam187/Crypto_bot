import sqlalchemy
import sqlite3
import pandas as pd
from data_cleaning import convert_from_db_to_df


def create_connection(database_name='crypto.db'):
    conn = sqlite3.connect(database_name)
    return conn


def create_cursor(connection):
    cursor = connection.cursor()
    return cursor


def create_table(connection, cursor):
    cursor.execute("""CREATE TABLE crypto_data (
        Name text, DateTime text, Price real)""")
    connection.commit()


def sql_query(connection, cursor, query_string= "SELECT * FROM crypto_data"):
    query = cursor.execute(f"{query_string}")
    return query


def add_df_stream_data(df, db_name='crypto.db', table_name='crypto_data'):
    """adds data after formatting to sqlite database using sqlalchemy"""
    conn_string = f'sqlite:///{db_name}'
    engine = sqlalchemy.create_engine(conn_string)
    df.to_sql(table_name, engine, if_exists='append', index=False)  


def select_all_from_db(conn, cursor):
    query = sql_query(conn, cursor)
    results = query.fetchall()
    return results   


if __name__ == "__main__":
    conn = create_connection()
    cursor = create_cursor(conn)
    res = select_all_from_db(conn, cursor)
    res_df = convert_from_db_to_df(res)
    print(res_df.to_string())
    print(res_df.info())


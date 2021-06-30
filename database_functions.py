import sqlalchemy
import sqlite3
import pandas as pd


def create_connection():
    conn = sqlite3.connect('crypto.db')
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
    conn_string = f'sqlite:///{db_name}'
    engine = sqlalchemy.create_engine(conn_string)
    df.to_sql(table_name, engine, if_exists='append', index=False)

        


if __name__ == "__main__":
    conn = create_connection()
    cursor = create_cursor(conn)
    # create_table(conn, cursor)
    query = sql_query(conn, cursor)
    conn.close()


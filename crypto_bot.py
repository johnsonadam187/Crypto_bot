import pandas as pd
import numpy as np
from binance import BinanceSocketManager
from binance.client import Client
from constants import api_key, secret_key
import asyncio
from database_functions import add_df_stream_data


async def basic_socket_manager(stock="BTCUSDT"):
    """Function for dealing with the websocket comms to retrieve the data"""
    client = Client(api_key, secret_key)
    manager = BinanceSocketManager(client)
    socket = manager.trade_socket(stock)
    await socket.__aenter__()
    msg = await socket.recv()
    return msg


def websocket_to_dataframe(socket_message):
    df1 = pd.DataFrame([socket_message])
    df1 = df1[['s', 'E', 'p']]
    df1.columns = ['Name', 'DateTime', 'Price']
    df1['DateTime'] = pd.to_datetime(df1['DateTime'], unit='ms')
    df1['Price'] = df1['Price'].astype(np.float64)
    return df1


def main():
    # TODO add scheduler to create loop for continual updating
    skt = asyncio.run(basic_socket_manager())
    df1 = websocket_to_dataframe(skt)
    add_df_stream_data(df1, db_name='crypto.db', table_name='crypto_data')
    print(df1)


if __name__=="__main__":
    main()

# TODO create scheduler
# TODO create manual db functions
# TODO add ability to visualise data
# TODO add ability for pulling multiple stocks/coins
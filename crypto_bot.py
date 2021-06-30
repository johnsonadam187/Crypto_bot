import pandas as pd
import numpy as np
from binance import BinanceSocketManager
from binance.client import Client
from constants import api_key, secret_key
import asyncio
from database_functions import add_df_stream_data
from data_cleaning import websocket_to_dataframe



async def basic_socket_manager(stock="BTCUSDT"):
    """Function for dealing with the websocket comms to retrieve the data"""
    client = Client(api_key, secret_key)
    manager = BinanceSocketManager(client)
    socket = manager.trade_socket(stock)
    await socket.__aenter__()
    msg = await socket.recv()
    return msg



def main():
    # TODO add scheduler to create loop for continual updating
    skt = asyncio.run(basic_socket_manager())
    df1 = websocket_to_dataframe(skt)
    add_df_stream_data(df1, db_name='crypto.db')


if __name__=="__main__":
    main()

# TODO create scheduler
# TODO create manual db functions
# TODO add ability to visualise data
# TODO add ability for pulling multiple stocks/coins
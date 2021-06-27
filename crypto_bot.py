import pandas as pd
import numpy as np
import sqlalchemy
from binance import BinanceSocketManager
from binance.client import Client
from constants import api_key, secret_key
import asyncio




def basic_socket_manager(stock="BTCUSDT"):
    client = Client(api_key, secret_key)
    manager = BinanceSocketManager(client)
    socket = manager.trade_socket(stock)
    return socket





if __name__=="__main__":
    skt = basic_socket_manager()
    print(skt)


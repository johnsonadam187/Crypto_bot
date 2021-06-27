import pandas as pd
import numpy as np
import sqlalchemy
from binance import BinanceSocketManager
from binance.client import Client

api_key = 'Buw50cp1iDCVR9ErLEgSsn2Y0Yk4ToVH1tbsZxQO2FLJOxdkgKwzTyui4tHx60vl'
secret_key  = 'UkW9eYi3X47Q0Pi1ZER6OK80vBmzX7cIXtpCqBI4FSGrzQIwyuKC00aPemBHmQ3K'

def basic_socket_manager():
    client = Client(api_key, secret_key)


    manager = BinanceSocketManager(client)




if __name__=="__main__":
    pass


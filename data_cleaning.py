import pandas as pd
import numpy as np
from crypto_bot import basic_socket_manager
import asyncio


def websocket_to_dataframe(socket_message):
    df1 = pd.DataFrame([socket_message])
    df1 = df1[['s', 'E', 'p']]
    df1.columns = ['Name', 'DateTime', 'Price']
    df1['DateTime'] = pd.to_datetime(df1['DateTime'], unit='ms')
    df1['Price'] = df1['Price'].astype(np.float64)
    return df1


if __name__=="__main__":
    skt = asyncio.run(basic_socket_manager())
    df = websocket_to_dataframe(skt)
    print(df.to_string())
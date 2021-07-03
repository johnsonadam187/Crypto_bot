import pandas as pd
from constants import dataframe_columns


def convert_from_db_to_df(results):
    results_df = pd.DataFrame(results)
    results_df.columns = dataframe_columns
    results_df['DateTime'] = pd.to_datetime(results_df['DateTime'])
    results_df["Price"] = pd.to_numeric(results_df["Price"])
    return results_df


if __name__ =="__main__":
    pass
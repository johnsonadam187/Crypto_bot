import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance as mpf
from database_functions import create_connection, create_cursor, select_all_from_db
from data_cleaning import convert_from_db_to_df


def simple_plot(df):
    sns.lineplot(df['DateTime'], df['Price'])
    plt.show()


def simple_line_plot_multi_coin(df):
    sns.lineplot(df['DateTime'], df['Price'], hue=df['Name'])
    plt.legend()
    plt.show()


def facet_grid(df, x='DateTime', y='Price', row_name='Name', plottype = sns.scatterplot):
    g = sns.FacetGrid(data = df, row=row_name, sharex=True, sharey=False)
    g.map(plottype, x, y)
    plt.show()


if __name__=="__main__":
    conn = create_connection()
    cursor = create_cursor(conn)
    res = select_all_from_db(conn, cursor)
    res_df = convert_from_db_to_df(res)
    sns.set_style('darkgrid')
    facet_grid(res_df, plottype=sns.lineplot)

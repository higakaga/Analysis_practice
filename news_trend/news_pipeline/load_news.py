from client_info import mysql_config
import pandas as pd
import pymysql
from utils import path_setup
from client_info import client_id, client_secret, mysql_config


def load_news_data():
    conn = pymysql.connect(**mysql_config)
    query = "SELECT * FROM news"
    df = pd.read_sql(query, conn)
    conn.close()

    df['pubDate'] = pd.to_datetime(df['pubDate'], errors='coerce')
    df = df.dropna(subset=['pubDate'])
    return df

import pymysql
from utils import path_setup
from client_info import mysql_config


def store_keywords_to_db(news_id, keywords):
    conn = pymysql.connect(**mysql_config)
    cursor = conn.cursor()
    for word, freq in keywords:
        cursor.execute('''
            INSERT INTO news_keywords (news_id, keyword, frequency)
            VALUES (%s, %s, %s)
        ''', (news_id, word, freq))
    conn.commit()
    conn.close()

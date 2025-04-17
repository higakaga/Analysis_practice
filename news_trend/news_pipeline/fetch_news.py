from datetime import datetime
import pymysql
import urllib.parse
import requests
from utils import path_setup
from client_info import client_id, client_secret, mysql_config


def get_news(query, display=20, start=1, sort='date'):
    enc_query = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/news.json?query={enc_query}&display={display}&start={start}&sort={sort}"

    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }

    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        news_items = res.json()['items']

        conn = pymysql.connect(**mysql_config)
        cursor = conn.cursor()

        for item in news_items:
            try:
                cursor.execute('''
                    INSERT IGNORE INTO news (title, description, link, pubDate)
                    VALUES (%s, %s, %s, %s)
                ''', (item['title'], item['description'], item['link'], item['pubDate']))
            except Exception as e:
                print("Insert error:", e)

        conn.commit()
        conn.close()
        print(f"{len(news_items)} items stored.")
    else:
        print("API Error:", res.status_code)


if __name__ == '__main__':
    get_news("대선")

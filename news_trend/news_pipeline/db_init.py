import pymysql
from utils import path_setup
from client_info import mysql_config

conn = pymysql.connect(**mysql_config)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS news (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title TEXT,
    description TEXT,
    link VARCHAR(500) UNIQUE,
    pubDate VARCHAR(100)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS news_keywords (
    id INT AUTO_INCREMENT PRIMARY KEY,
    news_id INT,
    keyword VARCHAR(100),
    frequency INT,
    FOREIGN KEY (news_id) REFERENCES news(id)
)
''')

conn.commit()
conn.close()
print("Tables created.")

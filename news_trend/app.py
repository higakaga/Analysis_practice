import streamlit as st
import pandas as pd
import pymysql
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from utils import path_setup
from client_info import mysql_config

st.set_page_config(page_title="뉴스 트렌드 분석", layout="wide")

# 데이터 불러오기


@st.cache_data
def load_data():
    conn = pymysql.connect(**mysql_config)
    news_df = pd.read_sql("SELECT * FROM news", conn)
    keyword_df = pd.read_sql("SELECT * FROM news_keywords", conn)
    conn.close()

    news_df['pubDate'] = pd.to_datetime(news_df['pubDate'], errors='coerce')
    return news_df.dropna(subset=['pubDate']), keyword_df


news_df, keyword_df = load_data()

# 📅 날짜 필터
dates = sorted(news_df['pubDate'].dt.date.unique())
selected_date = st.sidebar.selectbox("날짜 선택", dates, index=len(dates)-1)

# 선택된 날짜의 뉴스 수 시각화
st.title(f"📅 {selected_date} 뉴스 트렌드 분석")

# 뉴스 수
daily_news = news_df[news_df['pubDate'].dt.date == selected_date]
st.subheader("📈 수집된 뉴스 수")
st.write(f"총 {len(daily_news)}건")

# 키워드 상위 10개 시각화
daily_ids = daily_news['id'].tolist()
daily_keywords = keyword_df[keyword_df['news_id'].isin(daily_ids)]
top_keywords = daily_keywords.groupby(
    'keyword')['frequency'].sum().sort_values(ascending=False).head(10)

st.subheader("🔍 상위 키워드")
fig, ax = plt.subplots()
top_keywords.plot(kind='bar', ax=ax, color='skyblue')
ax.set_ylabel("빈도")
st.pyplot(fig)

# 워드클라우드
st.subheader("🌈 키워드 워드클라우드")
word_freq = dict(top_keywords)
wc = WordCloud(width=800, height=400, background_color='white',
               font_path='NanumGothic.ttf').generate_from_frequencies(word_freq)
st.image(wc.to_array())

# 뉴스 테이블
st.subheader("📰 뉴스 목록")
st.dataframe(daily_news[['title', 'link']])

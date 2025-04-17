import matplotlib.pyplot as plt
from load_news import load_news_data


def plot_news_by_date():
    df = load_news_data()
    daily = df.groupby(df['pubDate'].dt.date).size()

    plt.figure(figsize=(10, 4))
    daily.plot(kind='bar', color='steelblue')
    plt.title("날짜별 뉴스 수집 현황")
    plt.xlabel("날짜")
    plt.ylabel("기사 수")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    plot_news_by_date()

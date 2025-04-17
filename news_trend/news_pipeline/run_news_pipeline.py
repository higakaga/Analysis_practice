from load_news import load_news_data
from analyze_keywords import extract_keywords
from store_keywords import store_keywords_to_db


def run_keyword_extraction():
    df = load_news_data()

    for _, row in df.iterrows():
        combined = str(row['title']) + ' ' + str(row['description'])
        keywords = extract_keywords(combined)
        store_keywords_to_db(row['id'], keywords)


if __name__ == '__main__':
    run_keyword_extraction()

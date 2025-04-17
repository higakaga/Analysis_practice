from konlpy.tag import Okt
from collections import Counter

okt = Okt()


def extract_keywords(text, top_n=10):
    nouns = okt.nouns(text)
    filtered = [n for n in nouns if len(n) > 1]
    counter = Counter(filtered)
    return counter.most_common(top_n)

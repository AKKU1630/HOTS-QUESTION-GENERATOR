from collections import Counter
import re

def extract_topics(text, top_n=5):
    words = re.findall(r"\b[A-Za-z]{5,}\b", text.lower())
    common = Counter(words).most_common(top_n)
    return [word for word, _ in common]

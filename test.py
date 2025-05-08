import time
import pandas as pd
from utils import fetch_news_articles

companies = pd.read_excel("companies.xlsx")["Company"].tolist()

latencies = []
article_counts = []
summary_token_counts = []

for ticker in companies:
    start = time.time()
    articles = fetch_news_articles(ticker)
    elapsed = time.time() - start
    
    n = len(articles)
    if n == 0:
        continue

    article_counts.append(n)
    latencies.append(elapsed / n)  
    for a in articles:
        summary_token_counts.append(len(a["Summary"].split()))

avg_latency = sum(latencies) / len(latencies)
avg_articles  = sum(article_counts) / len(article_counts)
avg_summary_len = sum(summary_token_counts) / len(summary_token_counts)

print(f"Avg. latency per article: {avg_latency:.2f} s")
print(f"Avg. articles fetched per company: {avg_articles:.1f}")
print(f"Avg. summary length: {avg_summary_len:.1f} tokens")

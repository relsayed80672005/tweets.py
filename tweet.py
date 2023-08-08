import snscrape.modules.twitter as antwitter
import pandas as pd
query = "(hate OR kill OR screw) (#angry) lang:en untill:2023-01-24 since:2022-01-01 -filter:links -filter:replies"
tweets = []
limit = 100
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
  if len(tweets) == limit:
    break
  else:
    tweets.append([tweet.date, tweet.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
df.to_csv('dataset/tweets.csv')

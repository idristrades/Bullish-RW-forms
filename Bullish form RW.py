import snscrape.modules.twitter as sntwitter
import pandas as pd



date = '(since:2022-07-12)'
query = "files form RW" + date

tweets = []
limit = 7

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date,tweet.user.username, tweet.content, tweet.tcooutlinks])
        
df = pd.DataFrame(tweets, columns=['Date', 'Username', 'Tweet', 'Url'])
print(df)

#to save the data, use df.to_csv('tweets.csv')

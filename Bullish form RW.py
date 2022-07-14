import snscrape.modules.twitter as sntwitter
import pandas as pd

#update the date so you get the most recent RW forms

#############################
date = '(since:2022-07-01)'
#############################


query = "files form RW" + date

tweets = []

# to get more than the most recent 3 forms, change the number below
limit = 3


for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.content[0:5], tweet.tcooutlinks])
        
df = pd.DataFrame(tweets, columns=['Date', 'Ticker Symbol', 'Link to RW form'])
print(df)

#to save the data, use df.to_csv('tweets.csv')

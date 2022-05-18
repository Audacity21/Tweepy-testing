import tweepy
import config

client = tweepy.Client(config.BEARER_TOKEN)

#users = client.get_users(usernames='Audacity21')

#for user in users:
#    print(user)

tweets = client.get_users_tweets(id=config.USER_ID)

for tweet in tweets.data:
    print(tweet.id)
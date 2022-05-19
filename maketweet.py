import tweepy
import config

client = tweepy.Client(consumer_key=config.API_KEY,consumer_secret=config.API_SECRET, access_token=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_SECRET)

response = client.create_tweet(text="Smart Belt hive!")

print(response)
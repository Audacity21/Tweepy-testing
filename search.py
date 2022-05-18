import tweepy
import config

client = tweepy.Client(config.BEARER_TOKEN)

query = 'mancity OR manchester city -is:retweet'

response = client.search_recent_tweets(query=query, tweet_fields=['created_at', 'lang'], expansions=['author_id'])

users = {u['id']: u for u in response.includes['users']}

for tweet in response.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        print(tweet.id, user.username)
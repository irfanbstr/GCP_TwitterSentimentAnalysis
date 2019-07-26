#GET RECENT TWEETS, EXPORT TO JSON

import tweepy, json, time

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="yq6b8RykGgWJBKyFxyb0OjBoP"
consumer_secret="nBDdrquPmKOITE4a4mzHtFf5kVwd2a1IVZc0hYuXpDbBiOITwb"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="1326996704-fDpADUkOIn9jQYqwuLgZMoP4crEmUfp0ZgkGtdk"
access_token_secret="Km5vj5c6cXzOlLe2Vl7KeOQC0qPgdLUPK4TGr2PumSXtb"

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = tweepy.Cursor(api.search, q="prabowo -filter:retweets", result_type="recent", lang="id", tweet_mode='extended').items(10000)

data = {}
data['tweets'] = []

for item in search:
  data['tweets'].append({
    'name': item.user.name,
    'text': item.full_text,
    'location': item.user.location})
  
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
    
print('Done getting tweets.')
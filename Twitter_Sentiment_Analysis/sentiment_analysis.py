import tweepy
import textblob
import config

consumer_key = config.getConsumerKey()
consumer_secret = config.getConsumerSecret()
access_token = config.getAccessToken()
access_token_secret = config.getAccessTokenSecret()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def getSentiment(keyWord):
	tweets = api.search(keyWord)
	sentimentValues = []
	for tweet in tweets:
		if tweet.lang == "en":
			analysis = textblob.TextBlob(tweet.text)
			sentimentValues.append(analysis.sentiment.polarity)
	print(sentimentValues)
	Average_Sentiment = float(sum(sentimentValues)) / max(len(sentimentValues), 1)
	return Average_Sentiment

def collectSentiment():
	Avg_Sentiment = getSentiment('God')
	print("Average Sentiment: "+ str(Avg_Sentiment))
	return Avg_Sentiment

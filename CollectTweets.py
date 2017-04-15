
import tweepy
import csv
import io
from textblob import TextBlob
import re

try:
    from twitter_keys import *
except Exception:
    pass

outputFile = io.open( 'depression_tweets.csv', 'w', encoding='utf-8' )
writer = csv.writer( outputFile, delimiter='\t' )

#emoji pattern
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

class StreamListener( tweepy.StreamListener ):

	#override on_status to process tweets
	def  on_status( self, status ):
		
		#discard retweets
		if hasattr ( status, 'retweeted_status'):
			print ("Retweet... discarding")
			return

		#remove URLs and user mentions and emojis
		text = re.sub(r"(?:\@|https?\://)\S+", "", status.text)
		tweet = emoji_pattern.sub(r'', text) # no emoji

		#textblob doesn't handle string less than 3 characters long
		if len( tweet ) <  3:
			return

		#create a textblob
		blob = TextBlob( tweet )

		#read only english language tweets
		if blob.detect_language() != 'en':
			print ("Not english... discarding")
			return

		#find polarity of the tweet text
		sentiment = blob.sentiment
		polarity = sentiment.polarity

		#write to a csv file
		print("Found a matching tweet... writing to the file")
		print( tweet + " Polarity: " + str( polarity ) )
		#writer.writerow((status.text,status.user.location,status.coordinates,status.created_at,status.user.created_at))
		writer.writerow((tweet,polarity))

	#override on_error
	def on_error( self, status_code ):
		if status_code == 420:
			return False


def getTwitterAPIObject():
	auth = tweepy.OAuthHandler( CONSUMER_KEY, CONSUMER_SECRET )
	auth.set_access_token( ACCESS_TOKEN, ACCESS_TOKEN_SECRET )
	api = tweepy.API( auth )
	return api

twitterApi = getTwitterAPIObject()

streamListener = StreamListener()

stream = tweepy.Stream( auth=twitterApi.auth, listener=streamListener )

stream.filter( track=[ "depression", "PTSD", "depressed", "suicide" ] )

outputFile.close()
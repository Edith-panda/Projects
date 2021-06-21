#importing libraries
import tweepy
from time import sleep
#adding acces keys from twitter developers site
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
#authentication 
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)
#declaring the program for retweetimg the twitter
for tweet in tweepy.Cursor(api.search, q='#sunshine').items(5):
    try:
        print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')

        tweet.retweet()
        print('Responsing back....')

        # Where sleep(10), sleep is measured in seconds.
        # Change 10 to amount of seconds you want to have in-between retweets.
        # Read Twitter's rules on automation. Don't spam!
        sleep(10)

    # Some basic error handling. Will print out why retweet failed, into your terminal.
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break


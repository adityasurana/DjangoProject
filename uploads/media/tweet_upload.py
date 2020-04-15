from tweepy import OAuthHandler
from tweepy import API
import tweepy
import pandas as pd
import sys
import os

#Twitter API credentials
consumer_key = "d9QdJMWqs0ruF6MVYB2KVMrwE"
consumer_secret = "iGdgai3LXoaMVfdpofB5B2Upn8vIvpYjMFBgpfahpTLotUa3iQ"
access_token = "1096115767320313856-o3aWDahEVpPbA3Rcif3l5AwJMOwKZr"
access_token_secret = "R6ZWkjqyc96fAaeJg9fQOZBubCa9kSV04j4g4eRFMIEko"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet_id =        []
tweet_time =      []
tweet_text =      []
usr_screen_name = []
retweet_count =   []
like_count =      []

def get_all_tweets(screen_name):
    #print("camed in tweets_id of ", screen_name)
    alltweets = []
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    while len(new_tweets) > 0:
        #print("getting tweets before tweet id %s" % (oldest))
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        #print("...%s tweets downloaded so far" % (len(alltweets)))
        for tweet in alltweets:
            tweet_id.append(str(tweet.id_str))
            tweet_time.append(tweet.created_at)
            tweet_text.append(tweet.text.encode("utf-8"))
            usr_screen_name.append(screen_name)

dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)
twitter_kol = pd.read_excel("%s\\Twitter_ID.xlsx" %dir_path)
for j in twitter_kol.iloc[0:,0].unique():
    i=j.split('@')[1]
    try:
        get_all_tweets(i)
    except:
        pass

for i in tweet_id:
    tweets = api.get_status(int(i))
    try:
        retweet_count.append(tweets.retweet_count)
        like_count.append(tweets.favorite_count)
    except:
        retweet_count.append(0)
        like_count.append(0)

dir_path = os.path.dirname(os.path.realpath(__file__))
filePath = "%s\\twitter\\user_tweets.xlsx" %dir_path   
if os.path.exists(filePath):
    os.remove(filePath)
else:
    pass
        
df = pd.DataFrame(list(zip(usr_screen_name, tweet_id, tweet_time, tweet_text, retweet_count, like_count)),
                  columns = ['User Screen Name', 'Tweet Id', 'Tweet Time', 'Tweet Text', 'Retweet Count', 'Like Count'])
outputfile_path = "%s\\twitter\\user_tweets.xlsx" %dir_path
df.to_excel(outputfile_path, index=False)

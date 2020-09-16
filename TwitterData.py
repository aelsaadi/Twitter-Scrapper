#https://github.com/aelsaadi

from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

def percentage(part, whole):
    return 100 * float(part)/float(whole)

#Keys to access twitter API
consumerKey = 'enter your key here'
consumerSecret = 'enter your key here'
accessToken = 'enter your key here'
accessTokenSecret = 'enter your key here'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#input keyword and # of tweets to be analyzed
searchTweets = input("Enter keyword or hashtag to search: ")
NumSearchTerm = int(input("Enter how many tweets to analyze: "))

#searches for tweets
tweets = tweepy.Cursor(api.search, q=searchTweets).items(NumSearchTerm)

#variables for sentiment analysiss
positive = 0
negative = 0
neutral = 0
polarity = 0

#iterates through found tweets and adds polarities
for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if(analysis.sentiment.polarity == 0):
        neutral += 1
    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
    elif (analysis.sentiment.polarity > 0.00):
        positive += 1


positive = percentage(positive, NumSearchTerm)
negative = percentage(negative, NumSearchTerm)
neutral = percentage(neutral, NumSearchTerm)
polarity = percentage(polarity, NumSearchTerm)


positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

#prints out data and majority reaction
print("Sentiment Analysis for " + searchTweets + " by analyzing " + str(NumSearchTerm) + " Tweets.")
if (polarity == 0):
    print("Majority Neutral")
elif (polarity < 0.00):
    print("Majority Negative")
elif (polarity > 0.00):
    print("Majority Positive")

#design code for graph
labels = ['Positive ['+str(positive)+'%]', 'Neutral [' + str(neutral) + '%', 'Negative [' + str(negative) + '%']
sizes = [positive, neutral, negative]
colors = ['blue', 'gold', 'red']
patches, texts = plt.pie(sizes, colors = colors, startangle=90)
plt.legend(patches, labels, loc = "best")
plt.title('Sentiment Analysis for ' + searchTweets + ' by analyzing ' + str(NumSearchTerm) + ' Tweets.')
plt.axis('equal')
plt.tight_layout
plt.show()




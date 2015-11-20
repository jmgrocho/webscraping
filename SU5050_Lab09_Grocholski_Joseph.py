#------------------------------------------------------------------------------ 

# Joseph Grocholski
# 26 October 2015
# SU5050 - Data Mining
# Lab 9 - Twitter API Part 3

# Using Python Version 3.4

#------------------------------------------------------------------------------ 

import twitter 
import json
  
# Use first set of access tokens if possible
# Set access tokens 1
# Access token
OAUTH_TOKEN = ''
# Access token secret
OAUTH_SECRET = '' 
# Consumer key
CONSUMER_KEY =  'g1j1eTjJDUC68KbJ2olt48oGW' 
# Consumer secret
CONSUMER_SECRET = 'aiG0adKCO32lHDnaPi31MqYUMtfqqfMRhx53Sle1G17XqIrBrP'
#     Authenticate
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
#     Establish Twitter api
twitter_api = twitter.Twitter(auth=auth)

# Set access tokens 2
# Access token
OAUTH_TOKEN2 = '3950046370-lCK4FplVBkfA95n7dkshpRZtJU3tSoazfMSZHI5'
# Access token secret
OAUTH_SECRET2 = 'hz7Wh1xsKUdeUtUtN6kpR22m7bBtBDZnyu1g2soMARhde' 
# Consumer key
CONSUMER_KEY2 =  'y8Q4fjfunE5ClcdHaeDo0qliw' 
# Consumer secret
CONSUMER_SECRET2 = 'nFymAnWFVW2OFzenSljpDVctqQEuNwEsNGgLdoGkOyGwvxXN1A'
auth2 = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
#     Establish alternate Twitter api
twitter_api2 = twitter.Twitter(auth=auth2)


# Define string for search query
q = 'Houghton'
try:
    results = twitter_api.search.tweets(q=q)
except:
    results = twitter_api2.search.tweets(q=q) 


#===============================================================================
# JSON DUMPS
# Convert to JSON
# print("\nJSON Dumps:")
# dumpResults = json.dumps(results, indent=1)
# print('{}'.format(dumpResults))
# print("\n * * * * End of JSON dumps * * * * \n\n")
#===============================================================================

# [1a]  Determine number of Tweets returned by default
countStatus = len(results.get('statuses')) #integer
# Print the number of trends in the response
print("The number of trends in the response for {} is {}\n".format(q,countStatus))
# 15 tweets are returned by default, unless there are < 15 matches for the given query

# List of statuses (list of dict objects)
statuses = results['statuses']

# [1b]  Number of dict keys for each element of the statuses entry
count = 0
for item in statuses:
    count +=1
    print('Status {} - Number of keys:  {}'.format(count,len(item)))

# [1c] Print out the actual tweet for the first status in the list
print("\nThe actual tweet is given by the key 'text'.")
print("The first status in the {} query is:  {}\n".format(q,statuses[0].get('text')))

# [1d] Write a for loop to print out each tweet found in the search results
count = 1
# Loop through each trend in dict
print("List of 15 tweets for {}:".format(q))
for trend in results.get('statuses'):
    #     Get name from each trend in dict
    trendName = trend.get('text')
#     Add name to list
    print("{}:  {}".format(count, trendName))
    count += 1

# [1e] Write a for loop to also print out the user's screen name each tweet found in the search results
count = 1
# Loop through each trend in dict
print("\n\nList of 15 tweets for {} including username:".format(q))
for trend in results.get('statuses'):
    #     Get name from each trend in dict
    trendName = trend.get('text')
#     Get username
    userName = trend.get('user').get('name')
#     Add name to list
    print("{} - User {}:  {}".format(count, userName, trendName))
    count += 1
    
    
    
    
# [2a] 40 most recent tweets within 10 miles of Austin, Texas
# Set parameters
# Location of Austin, TX:  30.25, -97.75
q2 = ""
geocode2 = "30.25,-97.75,10mi"
count2 = "40"
type2 = "recent"
# query
results2 = twitter_api.search.tweets(q=q2,count=count2,result_type=type2,geocode=geocode2)

print("\n\nTweets of the 40 most recent tweets within 10 miles of Austin, TX with at least 1 hashtag:\n")
printCount = 1
# parse statuses
for tweet in results2.get('statuses'):
#     parse text in tweets
    tweetText = tweet.get('text')
#     parse entities in tweets
    tweetEntities = tweet.get('entities')
#     get hashtags from each tweet entity
    tweetHashtags = tweetEntities.get('hashtags')

#     Only print if the tweet has hashtags
    if tweetHashtags:
#         establish hashtag list variable        
        hashtagList = ""
#         add each hashtag to the list
        for tag in tweetHashtags:
            hashtagList += ('#'+(tag['text'] + ' '))
#         Display tweet number, number of hashtags, hashtags, and tweet text
        print("Austin Tweet #{} has {} hashtag(s):  {}".format(printCount, len(tweetHashtags), hashtagList))
        print("  {}\n".format(tweetText))
    printCount += 1
    
    
    
# [2b] 10 most popular tweets with the word 'donut' generated before October 21, 2015, listing tweets AND their 'favorite counts' only for those that were favorited at least 50 times. 
# Set parameters
# Location of Austin, TX:  30.25, -97.75
print("\n\nTweets of the 10 most popular tweets about donut generated before Oct 21 with at least 50 favorites\n")
q2b = "donut"
geocode2b = ""
until2b = "2015-11-19"
count2b = "10"
type2b = "popular"
# query
results2b = twitter_api.search.tweets(q=q2b,count=count2b,result_type=type2b,geocode=geocode2b,until=until2b)
printCount = 1
for tweet in results2b.get('statuses'):
#     Get favorite count
    tweetFav = tweet.get('favorite_count')
#     Only print tweet if it has at least 50 favorites
    if(tweetFav >= 50):       
        tweetText = tweet.get('text')
        print('{} - {}'.format(printCount, tweetText))
        print('  Marked as favorite {} times'.format(tweetFav))
    printCount += 1
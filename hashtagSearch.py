import twitter, time
from urllib.request import urlopen

startTime = time.time()

# Source for hashtags:  http://blog.buckybox.com/2012/01/hashtags-for-local-food/
# list of hashtags
hashtags = ['agriculture','farming','farm','garden','ag','agchat','foodchat','AgGen','SustainableAg','SustAg','Agroecology','FoodSystem','profood','localfood','eatlocal','locavore','realfood','SlowFood','slowmoney','UrbanAg','csa','foodhub','permaculture','organic','foodrevolution','urbanfarming','youthurbanfarming']



def hashtagTwitterSearch(city,lat,lon):
#     Name output file
    filename = city + "HashtagsMatch.txt"
#     Create output file with write access
    writeFile = open(filename,'w')
    writeFile.write("**********  {} Urban Farming Hashtags  **********".format(city))
#     timestamp
    writeFile.write("\n         Last Updated {}\n\n".format(time.ctime()))
#     Set query geocode
    geocode = str(lat) + "," + str(lon) + ",20mi"
#     Query each tag in list of urban farming hashtags
    for tag in hashtags:
#         set text for query
        query = "#" + tag
#         Uncomment to Search without hashtag
        query = tag               
        try:
            #       Access token
            OAUTH_TOKEN = '3950046370-lCK4FplVBkfA95n7dkshpRZtJU3tSoazfMSZHI5'
            #    Access token secret
            OAUTH_SECRET = 'hz7Wh1xsKUdeUtUtN6kpR22m7bBtBDZnyu1g2soMARhde' 
            #    Consumer key
            CONSUMER_KEY =  'y8Q4fjfunE5ClcdHaeDo0qliw' 
            #    Consumer secret
            CONSUMER_SECRET = 'nFymAnWFVW2OFzenSljpDVctqQEuNwEsNGgLdoGkOyGwvxXN1A'
            #    Authenticate
            auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
            #    Establish Twitter api
            twitter_api = twitter.Twitter(auth=auth)
            #    query
            results = twitter_api.search.tweets(q=query,count=50,geocode=geocode)
            #    Try second set of authentication keys
        except:
            OAUTH_TOKEN = ''
            #    Access token secret
            OAUTH_SECRET = '' 
            #    Consumer key
            CONSUMER_KEY =  'g1j1eTjJDUC68KbJ2olt48oGW' 
            #    Consumer secret
            CONSUMER_SECRET = 'aiG0adKCO32lHDnaPi31MqYUMtfqqfMRhx53Sle1G17XqIrBrP'
            #    Authenticate
            auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
            #    Establish Twitter api
            twitter_api = twitter.Twitter(auth=auth)
            #    query
            results = twitter_api.search.tweets(q=query,count=50,geocode=geocode)
    
        writeFile.write("\n------------------------------------\n\nTweets matching \"{}\" within 20 miles of {}:\n".format(query,city))
        
        printCount = 1
        # parse statuses
        for tweet in results.get('statuses'):
        #     parse text in tweets
            tweetText = tweet.get('text')
        #     parse entities in tweets
            tweetEntities = tweet.get('entities')
        #     get hashtags from each tweet entity
            tweetHashtags = tweetEntities.get('hashtags')
#             print tweet
            writeFile.write("\n{} - {}\n".format(printCount,tweetText))
        #    print if the tweet has hashtags
            if tweetHashtags:
        #         establish hashtag list variable        
                hashtagList = ""
        #         add each hashtag to the list
                for tag in tweetHashtags:
                    hashtagList += ('#'+(tag['text'] + ' '))
        #         Display tweet number, number of hashtags, hashtags, and tweet text
                writeFile.write("Tweet hashtag(s):  {} - {}\n".format(len(tweetHashtags), hashtagList))
            
            printCount += 1
        
    writeFile.close()
    print("Done writing output to {}".format(filename))   
        

hashtagTwitterSearch("Detroit", 42.331, -83.046)  

endtime = time.time()
eTime = endtime - startTime

print("Finished running script in {} seconds".format(eTime))  



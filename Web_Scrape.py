# import urllib2
import time
startTime = time.time()

import twitter, re
from urllib.request import urlopen


# Define twitterSearch function
def twitterSearch(name,lat,lon,writeFile):
    
    geocode = str(lat) + "," + str(lon) + ",20mi"
    query = name.replace("&amp;#039;","'")
    try:
            
        # Access token
        OAUTH_TOKEN = '3950046370-lCK4FplVBkfA95n7dkshpRZtJU3tSoazfMSZHI5'
        # Access token secret
        OAUTH_SECRET = 'hz7Wh1xsKUdeUtUtN6kpR22m7bBtBDZnyu1g2soMARhde' 
        # Consumer key
        CONSUMER_KEY =  'y8Q4fjfunE5ClcdHaeDo0qliw' 
        # Consumer secret
        CONSUMER_SECRET = 'nFymAnWFVW2OFzenSljpDVctqQEuNwEsNGgLdoGkOyGwvxXN1A'
        #     Authenticate
        auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
        #     Establish Twitter api
        twitter_api = twitter.Twitter(auth=auth)
        
    #     query
        results = twitter_api.search.tweets(q=query,count=50,geocode=geocode)
    
    except:
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
        
        #     query
        results = twitter_api.search.tweets(q=query,count=50,geocode=geocode)
    
    writeFile.write("\n------------------------------------\n\nTweets matching \"{}\" within 20 miles of Detroit:".format(name))
    
    printCount = 1
    # parse statuses
    for tweet in results.get('statuses'):
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
            writeFile.write("Tweet hashtag(s):  {} - {}\n".format(len(tweetHashtags), hashtagList))
        writeFile.write("\n{} - {}\n".format(printCount,tweetText))
        printCount += 1
# Define scrape function
def scrape(city,lat,lon):
    scrapeTimeStart = time.time()
    cityName = str(city)
    latLow = lat - 1
    latHigh = lat + 1
    lonLow = lon -1
    lonHigh = lon +1
    filename1 = cityName + "Farms.txt"
    filename2 = cityName + "FarmsLatLon.txt"
    filename3 = cityName + "FarmsDetails.txt"
    filename4 = cityName + "FarmsTwitter.txt"
     
    # Create output files for Detroit Farms
    outputFile = open(filename1,'w')
    outputFile.write("Last updated:  {}\n------------------------------------\n\n".format(time.ctime())) 
    outputFile2 = open(filename2,'w')
    outputFile2.write("Last updated:  {}\n------------------------------------\n\n".format(time.ctime())) 
    outputFile3 = open(filename3,'w')
    outputFile3.write("Last updated:  {}\n------------------------------------\n\n".format(time.ctime()))  

# Search for city in list of farms, within 1 degree of coordinates
#     initialize list
    cityFarmList = []
    count = 0
    for farm in farmList:
#         find farms in city, ignoring farms that are named "Garden"
        if(re.search(farm['City'], cityName, re.IGNORECASE) and farm['Name'] != 'Garden'):    
#         write farm names to file
            outputFile.write('Farm:  {}\n'.format(farm['Name'].replace("&amp;#039;","'")))
#         Write lat/lon values to file
#         Verify lat/long
            if float(farm['Latitude']) > latLow and float(farm['Latitude']) < latHigh and float(farm['Longitude']) > lonLow and float(farm['Longitude']) < lonHigh :
                outputFile2.write('{}, {}, {}\n'.format(farm['Name'].replace("&amp;#039;","'").replace("&amp;amp;","&").replace('amp;',''), farm['Latitude'], farm['Longitude']))
                count += 1
                cityFarmList.append(farm)
    #         Write details of each farm to file
            outputFile3.write('Location:  {}, {}\n'.format(farm['Latitude'],farm['Longitude']))
            outputFile3.write('Map Pin Type:  {}\n'.format(farm['Type']))
            outputFile3.write('ID:  {}\n'.format(farm['ID']))
            outputFile3.write('Name:  {}\n'.format(farm['Name']))
            outputFile3.write('Size:  {}\n'.format(farm['Size']))
            outputFile3.write('City:  {}\n'.format(farm['City']))
            outputFile3.write('State:  {}\n'.format(farm['State']))
            outputFile3.write('ZIP:  {}\n'.format(farm['ZIP']))
            outputFile3.write('---------------------------------------------------\n')
                 
       
    # Close output files
    print("\nDone writing output to {}".format(filename1))
    outputFile.close()
    print("Done writing output to {}".format(filename2))
    outputFile2.close()
    print("Done writing output to {}".format(filename3))
    outputFile3.close()
    
   
    print("\nFound {} valid farms in {}".format(count,cityName))

    print("starting Twitter search")

    # Create file for Twitter output
    outputFile4 = open(filename4,'w')
    outputFile4.write("Last updated:  {}".format(time.ctime()))
    for farm in cityFarmList:
        #Run Twitter query
        try:
            twitterSearch(str(farm['Name']),str(farm['Latitude']),str(farm['Longitude']),outputFile4)
        except:
            "reached end of rate limit"
    print("Done writing output to {}".format(filename4))
#     Close file
    outputFile4.close()
    scrapeTimeEnd = time.time()
    scrapeTime = scrapeTimeEnd - scrapeTimeStart
    print(" * * finished scrape of {} in {} seconds".format(cityName,scrapeTime))
    


# Parse UrbanFarming.org site to get initial list of farms
myurl = "http://www.urbanfarming.org/garden-locations.html"

with urlopen('http://www.urbanfarming.org/garden-locations.html') as response:
    html = response.read()

# decode html to convert byte to string
mystring = html.decode("ISO-8859-1")
# Split html by line
mystring = mystring.split('\n')

count=0

# create list of farm dictionaries
farmList = []
# Open gardens output file
outputFile = open("gardens.txt",'w')

# parse the html
for item in mystring:
    count += 1
#     search for valid lines of html which indicate farms
    if 'addMarker(' in item and ',' in mystring[count+1] and 't' not in mystring[count+1]:
        
#         write attributes of each farm to the file 
#         Latitude
        lat = mystring[count].replace(',','').replace('"','').strip()
        outputFile.write('Latitude:  {}\n'.format(lat))
       
#        Longitude
        long = mystring[count+1].replace(',','').replace('"','').strip()
        outputFile.write('Longitude:  {}\n'.format(long))
       
#        Pin/farm type
        pinType = mystring[count+2].replace(',','').replace('"','').strip()
        outputFile.write('Map Pin Type:  {}\n'.format(pinType))
       
#        Urbanfarming.org farm ID
        id = mystring[count+3].replace(',','').replace('"','').strip()
        outputFile.write('ID:  {}\n'.format(id))
       
#        Farm name 
        name = mystring[count+4].replace(',','').replace('"','').replace("&amp;#039;","'").strip()
        outputFile.write('Name:  {}\n'.format(name))
       
#        Farm size
        size = mystring[count+5].replace(',','').replace('"','').strip()
        outputFile.write('Size:  {}\n'.format(size))
       
#        City
        city = mystring[count+6].replace(',','').replace('"','').strip()
        outputFile.write('City:  {}\n'.format(city))
       
#        State abbreviation
        state = mystring[count+7].replace(',','').replace('"','').strip()
        outputFile.write('State:  {}\n'.format(state))
       
#        ZIP code
        zip = mystring[count+8].replace(',','').replace('"','').strip()
        outputFile.write('ZIP:  {}\n'.format(zip))
        outputFile.write('---------------------------------------------------\n')
       
#         create a dictionary object for farm
        farmDict = {'Latitude': lat, 'Longitude': long, 'Type': pinType,'ID': id,'Name': name,'Size': size, 'City': city, 'State': state, 'ZIP': zip}
#         add farm dictionary to the list of farms
        farmList.append(farmDict)
              
# Close output file
outputFile.close()
print("Done writing output to gardens.txt")

scrape("Detroit",42.331,-83.046)
# scrape("Harare",-17.864,31.030)
# scrape("Dakar",14.693,-17.447)
# scrape("Ho Chi Minh",10.777,106.701)
scrape("St. Louis",38.627,-90.198)

endTime = time.time()
elapsedTime = endTime - startTime
etimeMin = int(elapsedTime/60)
etimeSec = elapsedTime - (60 * etimeMin)
print("\n\n********************************************************************\n\nfinished running script in {} minutes, {} seconds".format(etimeMin,etimeSec))

# Specific Detroit web scrape
#===============================================================================
# 
# # Create output files for Detroit Farms
# outputFile = open("DetroitFarms.txt",'w') 
# outputFile2 = open("DetroitFarmsLatLon.txt",'w')
# outputFile3 = open("DetroitFarmsDetails.txt",'w') 
# 
# # Search for Detroit in list of farms
# detroitFarmList = []
# count = 0
# for farm in farmList:
#     if(farm['City'] == 'Detroit' or farm['City'] == 'detroit' or farm['City'] == 'DETROIT') and farm['State'] == 'MI' and farm['Name'] != 'Garden':
#        
#        
# #         write farm names to file
#         outputFile.write('Farm:  {}\n'.format(farm['Name'].replace("&amp;#039;","'")))
# #         Write lat/lon values to file
# #         Verify lat/long
#         if float(farm['Latitude']) > 41 and float(farm['Latitude']) < 43 and float(farm['Longitude']) < -82 and float(farm['Longitude']) > -84 :
#             outputFile2.write('{}, {}, {}\n'.format(farm['Name'].replace("&amp;#039;","'").replace("&amp;amp;","&").replace('amp;',''), farm['Latitude'], farm['Longitude']))
#             count += 1
#             detroitFarmList.append(farm)
# #         Write details of each farm to file
#         outputFile3.write('Location:  {}, {}\n'.format(farm['Latitude'],farm['Longitude']))
#         outputFile3.write('Map Pin Type:  {}\n'.format(farm['Type']))
#         outputFile3.write('ID:  {}\n'.format(farm['ID']))
#         outputFile3.write('Name:  {}\n'.format(farm['Name']))
#         outputFile3.write('Size:  {}\n'.format(farm['Size']))
#         outputFile3.write('City:  {}\n'.format(farm['City']))
#         outputFile3.write('State:  {}\n'.format(farm['State']))
#         outputFile3.write('ZIP:  {}\n'.format(farm['ZIP']))
#         outputFile3.write('---------------------------------------------------\n')
#         
# 
#        
#        
# # Close output file
# print("\nDone writing output to DetroitFarms.txt")
# outputFile.close()
# print("Done writing output to DetroitFarmsLatLon.txt")
# outputFile2.close()
# print("Done writing output to DetroitFarmsDetails.txt")
# outputFile3.close()
#    
# print("\nFound {} valid farms in Detroit, MI".format(count))
# 
# print("starting Twitter search")
# 
# # Create file for Twitter output
# outputFile = open("DetroitFarmsTwitter.txt",'w')
# for farm in detroitFarmList:
#     #Run Twitter query
#     try:
#         twitterSearch(str(farm['Name']),str(farm['Latitude']),str(farm['Longitude']),outputFile)
#     except:
#         "reached end of rate limit"
# print("\nDone writing output to DetroitFarmsTwitter.txt")
# outputFile.close()
#     
#     
#===============================================================================
# Web scraping function

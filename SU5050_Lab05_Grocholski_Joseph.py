#------------------------------------------------------------------------------ 
# Joseph Grocholski
# 30 September 2015
# SU5050 - Data Mining
# Lab 5 - Web Scraping

# Using Python Version 3.4

# This program displays the rank, name, and population of the 100 most populous cities in the United States according to city-data.com
#------------------------------------------------------------------------------ 
 

# Import urlopen function from the urllib.request module
from urllib.request import urlopen
# Set URL for page that is being scraped
myurl = 'http://www.city-data.com/top1.html'
# Read html code line by line and store as a list of binary objects
rawhtml = urlopen(myurl).readlines()

# Establish count variable for loop
count = 0
# Establish list of cities variable
listOfCities = ""

# Parse the html to find the top 100 cities
for line in rawhtml:
#     Convert from binary to string
    line = line.decode()
#     Determine if line contains a city name
    if ("http://pics3.city-data.com/sge.gif") in line:
#         Increase count by 1
        count = count +1
#         Split the raw html into two parts, the 2nd is the beginning of the city name string
        lineCity1 = line.split(".html\'>")
#         Split the remaining raw html into two parts, the 1st is the end of the city name string
        lineCity2 = lineCity1[1].split("</a>")
        lineCity = lineCity2[0]
#         Split the remaining raw html into two parts, the 2nd is the beginning of the city population
        linePop1 = lineCity2[1].split("(pop ")
#         Split the remaining raw html into two parts, the 1st is the end of the population        
        linePop2 = linePop1[1].split(")</td>")
        linePop = linePop2[0]
#         Add rank, name, population to list of cities
        listOfCities = listOfCities + str(count) + " " + lineCity + " " + linePop + "\n"

# Display the list of cities on the console
print(listOfCities)
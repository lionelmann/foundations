# Read Text
# Check text for curse words
#

import urllib

def read_text():
    quotes = open("/Users/lmann/Desktop/udacity-python/movie_quotes.txt")
    contents_of_file= quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.purgomalum.com/service/xml?text="+text_to_check) #module in python called urllib which has a function called urlopen
    output = connection.read()
    # print(output)
    connection.close()
    if "*" in output:
        print ("yikes")
    else:
        print("No")

read_text()


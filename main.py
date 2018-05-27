from twitter import Twitter, OAuth
import tweepy
import json
import re
from termcolor import colored
from textblob import TextBlob
from paralleldots import set_api_key, get_api_key, sentiment
import nltk
from nltk.corpus import *
from nltk import Counter
global tweets
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

print ("\033[35;40m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print (colored("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Welcome To TwitterBOT " , color= 'red', attrs=['bold']))

#-----------------------------------------------------------------------------------------------------------------------
# REQUIRED CREDENTIALS
API_KEY = '2pfABtRSFGD7HMxBdHiOOwWfP'
API_SECRET = '7b1bKAb2iJmicmEQL0cgtTROvhFhzktGbWCmExSoz0nRfoUOHG'

ACCESS_TOKEN = '1000470339057430528-Lj84LYKg09FPw8lhxc14X1KKEevCMc'
ACCESS_TOKEN_SECRET = 'x0UGvVS0K4qexUuAPcvDLsUw5UTnmlcZ2rarzCj2etEs9'

#-----------------------------------------------------------------------------------------------------------------------

twitter_oauth = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET)
twitter = Twitter(auth = twitter_oauth)

oauth = tweepy.OAuthHandler(API_KEY, API_SECRET)
oauth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(oauth)

#-----------------------------------------------------------------------------------------------------------------------

#FOR DISPLAYING MY ACCOUNT DETAILS
def details():
    myaccount = api.me()
    print (colored("\n Personal Details", color='blue', attrs=['underline']))
    print 'Name: '  + myaccount.name
    print 'Friends: ' + str(myaccount.friends_count)
    print (colored("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
                   color='blue'))
#-----------------------------------------------------------------------------------------------------------------------

# FOR GETTING QUERY

def get_tweets(query):
    tweets = twitter.search.tweets(q='#' +query, count=200)
    return tweets
    print (colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
                   color='blue'))

#-----------------------------------------------------------------------------------------------------------------------

# FOR GETTING NUMBER OF FOLLOWERS

def get_num_followers(query):
    num_followers = 0
    tweets = get_tweets(query)
    #print type(tweets)
    for each_tweet in tweets['statuses']:
        print (colored("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
                       color= 'green'))
        print "Name: " + each_tweet['user']['screen_name']
        print "Followers: " + str(each_tweet['user']['followers_count'])
        # print each_tweet['user']['location']
        num_followers += each_tweet['user']['followers_count']
    return  num_followers
    print (colored("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
                   color='blue'))
#-----------------------------------------------------------------------------------------------------------------------

# FOR GETTING SENTIMENTS

def get_sentiments(query):
    p = 0
    n=0
    ne = 0
    set_api_key('2Z4UlTNyfjXwIn5CGLy4EvS5IaySrLFfJDiMSPGCo3o')
    get_api_key()
    public_tweets = api.search(query)
    for tweet in public_tweets:
        text = tweet.text
        print (colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
                       color='blue'))
        print (colored(tweet.text, color='red'))
        r = sentiment(tweet.text)
        print(colored(r, color= 'red'))
        result = r['sentiment']
        if result == "positive":
            p = p+1
        elif  r['sentiment'] == "neutral":
            n = n+1
        else:
            ne = ne+1
    print (colored("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
                   color='green'))
    print "Maximum positive comments: ", p
    print "Maximum neutral comments: ", n
    print "Maximum negative comments: ", ne
    print (colored("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
                   color='green'))

#-----------------------------------------------------------------------------------------------------------------------

# FOR GETTING LOCATION, LANGUAGE AND TIME ZONE

def llt(query):

    public_tweets = get_tweets(query)
    location = {}
    language = {}
    time_zone = {}
    for tweet in public_tweets['statuses']:
        loc = tweet['user']['location']
        lang = tweet['user']['lang']
        tz = tweet['user']['time_zone']

        if loc in location:
            location[loc] += 1
        else:
            location[loc] = 1
        if lang in language:
            language[lang] += 1
        else:
            language[lang] = 1
        if tz in time_zone:
            time_zone[tz] += 1
        else:
            time_zone[tz] = 1
    if None in time_zone:
        del time_zone[None]
    if '' in time_zone:
        del time_zone['']
    if '' in language:
        del language['']
    if '' in location:
        del location['']
    if None in location:
        del location[None]
    if None in language:
        del language[None]
    language_count = dict(Counter(language).most_common(4))
    print (colored("language: ", color='green', attrs=['bold']))
    print language_count
    location_count = dict(Counter(location).most_common(4))
    print (colored("locations: ", color='green', attrs=['bold']))
    print location_count
    time_zone_count = dict(Counter(time_zone).most_common(4))
    print (colored("Time Zone: ", color='green', attrs=['bold']))
    print time_zone_count
    print (colored("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
                       color='red'))

# -----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

#RETRIVING THE TWEETS

def GetSearch(query):
    tweets = get_tweets(query)
    print json.dumps(tweets)

#-----------------------------------------------------------------------------------------------------------------------

# FOR COMPARISION OF MODI AND TRUMP TWEETS

def Comparision():

    # FOR MODI
    count = 0
    new_tweets = api.user_timeline(screen_name = '@narendramodi', count = 200, tweet_mode='extended')
    for tweet in new_tweets:
        print(tweet.full_text)
        text = tweet.full_text
        temp = []
        temp.append(text)
        temp1 = temp
        words = re.sub(r"http\S+", "", str(temp1))
        word = words.split()
        for i in word:
            i = i.upper()
            if i == "USA" or i == "US" or i == "America" or i == "United States of America":
                count = count + 1
    print (colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
                   color='green'))
    print "Number of times Narendra Modi mentioned 'USA', 'US', 'United States Of America:' or 'America':" , count


    #FOR TRUMP
    count1 = 0
    new_tweets = api.user_timeline(screen_name='@realDonaldTrump', count=200, tweet_mode='extended')
    for tweet in new_tweets:
        print(tweet.full_text)
        text = tweet.full_text
        temp = []
        temp.append(text)
        temp1 = temp
        words = re.sub(r"http\S+"," ", str(temp1))
        word = words.split()
        for i in word:
            i = i.lower()
            if i == "India" or i == "INDIA":
                count1 = count1 + 1
    print "Number of times Donald Trump mentioned 'India': ", count1
    print (colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
                   color='green'))

#-----------------------------------------------------------------------------------------------------------------------

# FOR DETERMINING TOP USAGE STOPWORDS

def Topusage():
    new_tweets = api.user_timeline(screen_name='@narendramodi', count=200, tweet_mode='extended')
    for tweet in new_tweets:
        #print(tweet.full_text)
        temp = []
        temp.append(tweet.full_text)
        temp1 = temp
        import re
        words = re.sub(r"http\S+"," ", str(temp1))
        word = words.split()
        word1 = [w for w in word if w in stop_words]
        for w in word1:
            if w not in stop_words:
                word1.append(w)
        num = Counter(word1).most_common(10)
        #print word1
        print(num)

#-----------------------------------------------------------------------------------------------------------------------

# FOR UPDATING STATUS

def tweet_status():
    status = raw_input("Enter your new tweet: ")
    api.update_status(status)
    print("Tweeted: {}".format(status))
    print (colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++",
                   color='red'))

#-----------------------------------------------------------------------------------------------------------------------

# MAIN FUNCTION

def main():
    print (colored("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
                   color='red'))
    while (True):
        user_choice = input("\nWhat would you like to do? Choose the option \n"
                   "1. Display my Twitter details.\n"
                   "2. Retreiving the tweets.\n"
                   "3. Count the total number of followers. \n"
                   "4. Determine the sentiments of people Tweeting by using a certain hash tag. \n"
                   "5. Determining the location, timezone and language of people Tweeting using a certain hash tag. \n"
                   "6. Comparision of tweets by Narendera Modi and Donald Trump. \n"
                   "7. Determining Top Usage. \n"
                   "8. Tweet a message from your account. \n"
                   "9. Exit\n"
                   "Enter your Choice: ")

        if user_choice == 1:
         details()

        elif user_choice == 2:
         user_input = raw_input("Enter the has tag: ")
         GetSearch(user_input)

        elif user_choice == 3:
         user_input = raw_input("Enter the has tag: ")
         print colored("Maximum number of people who have seen this has tag are: %s ", 'green') % (
             get_num_followers(user_input))

        elif user_choice == 4:
         user_input = raw_input("Enter the has tag: ")
         get_sentiments(user_input)

        elif user_choice == 5:
         user_input = raw_input("Enter the has tag: ")
         llt(user_input)

        elif user_choice == 6:
         Comparision()

        elif user_choice == 7:
         Topusage()

        elif user_choice == 8:
         tweet_status()

        elif user_choice == 9:
         break
        else:
         print("Wrong choice. Try again.")
         exit()
main()
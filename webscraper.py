from bs4 import BeautifulSoup
import requests
import json

url = 'https://twitter.com/BuzzFeed'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")


for tweet in content.findAll('div', attrs={"class": "content"}):
    tweetObject = {
        #"tweet": tweet.find('p', attrs={
        # "class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
        #"likes": tweet.find('span', attrs={
        # "class":"ProfileTweet-actionCountForPresentation"})
        "emoji":tweet.find('img',attrs={
            "class":"Emoji Emoji--forText"
        })
    }
    print(tweetObject)
 



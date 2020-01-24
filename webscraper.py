from bs4 import BeautifulSoup
import requests
import json

url = 'https://twitter.com/BuzzFeed'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")



for tweetList in content.findAll('div', attrs={"class": "content"}):
    tweetObject = {
        "tweet": tweetList.find('p', attrs={"class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
    }
    print(tweetObject)



from bs4 import BeautifulSoup
import requests
import json

url = 'https://twitter.com/itsyourhoney'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

for tweetList in content.findAll('div', attrs={"class": "content"}):
    tweetObject = {
        "tweet": tweetList.find('p', attrs={"class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
    }
    print(tweetObject)

'''tweetArr = []
for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
    tweetObject = {
        "author": tweet.find('h2', attrs={"class": "author"}).text.encode('utf-8'),
        "date": tweet.find('h5', attrs={"class": "dateTime"}).text.encode('utf-8'),
        "tweet": tweet.find('p', attrs={"class": "content"}).text.encode('utf-8'),
        "likes": tweet.find('p', attrs={"class": "likes"}).text.encode('utf-8'),
        "shares": tweet.find('p', attrs={"class": "shares"}).text.encode('utf-8')
    }
    tweetArr.append(tweetObject)

tweetArr = tweetArr[1:]
with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)'''
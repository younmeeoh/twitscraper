#converting scraped data to JSON - into Dicts. form of key
#each tweet is in <div> element with class name "tweetcontainer"

for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
    tweetObject = {
        "author": tweet.find('h2', attrs={"class": "author"}).text.encode('utf-8'),
        "date": tweet.find('h5', attrs={"class": "dateTime"}).text.encode('utf-8'),
        "tweet": tweet.find('p', attrs={"class": "content"}).text.encode('utf-8'),
        "likes": tweet.find('p', attrs={"class": "likes"}).text.encode('utf-8'),
        "shares": tweet.find('p', attrs={"class": "shares"}).text.encode('utf-8')
    }
    #Saving the scraped data as JSON.
    #append each tweetObject to the array.
    tweetArr.append(tweetObject)

for item in tweetArr:
    print(item)
#have Python generate written new file called twitterData.
with open('twitterData.json','w') as outfile:
    json.dump(tweetArr, outfile)





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
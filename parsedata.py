import json 

#with will ensure the file is closed again when done
#open() produces a file that json.load() can read from
with open('twitterData.json') as json_data:
#create variable named jsonData to contain the twitterData.
#json.loads() takes a JSOn encoded string
    jsonData = json.load(json_data)
#print all dates of the tweet
for i in jsonData:
    print(i[jsonData])
# Retrieve news items via API, deliver via email.

import getNews
import sendMail
import json

subject = input("What topic would you like to search for?:")
destination = input("Enter Email address:")

with open('data/newsApiKeyFile.json') as f:
    content = json.load(f)
    apiKey = content['key']

articles = getNews.retrieve(apiKey, subject)

body = f"Subject: {subject} News of the Day!\n"
for article in articles:
    title = str(article['title'])
    description = str(article['description'])
    link = str(article['url'])

    body = body + f"Title: {title}\n" \
                  f"{description}\n" \
                  f"{link}\n\n"

body = body.encode('ascii','ignore')

sendMail.send(destination, body)

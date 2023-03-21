# Retrieve news items via API, deliver via email.

import requests
import json
import sendMail

apiKey = "ceff54e923a34b8288a7f82f1ac62727"
url = "https://newsapi.org/v2/everything?q=Trump&sortBy=publishedAt&apiKey=ceff54e923a34b8288a7f82f1ac62727"

request = requests.get(url)
content = request.json()

body = "Subject: News of the Day!\n"
for article in content['articles']:
    title = article['title']
    description = article['description']
    body = body + f"Title: {title}\n" \
                  f"{description}\n\n"

body = body.encode('ascii','ignore')

sendMail.send("robert.lagrasse@gmail.com", body)

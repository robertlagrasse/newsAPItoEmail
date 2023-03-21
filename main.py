# Retrieve news items via API, deliver via email.

import getNews
import sendMail
import json

subject = "pandas"
articles = getNews.retrieve(subject)

print(json.dumps(articles[0], indent=4))
body = "Subject: News of the Day!\n"
for article in articles:
    title = str(article['title'])
    description = str(article['description'])
    link = str(article['url'])

    body = body + f"Title: {title}\n" \
                  f"{description}\n" \
                  f"{link}\n\n"

body = body.encode('ascii','ignore')

sendMail.send("robert.lagrasse@gmail.com", body)

import requests
import json
def retrieve(apiKey= "", topic="", language="", start_date="", end_date=""):
    url = f"https://newsapi.org/v2/everything?q={topic}&" \
          f"sortBy=publishedAt&" \
          f"language={language}&" \
          f"from={start_date}&" \
          f"to={end_date}&" \
          f"apiKey={apiKey}"
    request = requests.get(url)
    content = request.json()
    try:
        return content['articles']
    except:
        return []

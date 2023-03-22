import requests
import json
def retrieve(apiKey= "", topic="", language="", start_date="", end_date=""):
    # apiKey = "ceff54e923a34b8288a7f82f1ac62727"
    url = f"https://newsapi.org/v2/everything?q={topic}&" \
          f"sortBy=publishedAt&" \
          f"language={language}&" \
          f"from={start_date}&" \
          f"to={end_date}&" \
          f"apiKey={apiKey}"
    request = requests.get(url)
    content = request.json()
    return content['articles']

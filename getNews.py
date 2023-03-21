import requests
import json
def retrieve(topic=""):
    apiKey = "ceff54e923a34b8288a7f82f1ac62727"
    url = f"https://newsapi.org/v2/everything?q={topic}&" \
          f"sortBy=publishedAt&" \
          f"language=en&" \
          f"apiKey={apiKey}"
    request = requests.get(url)
    content = request.json()
    return content['articles']

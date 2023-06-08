import requests

api_key = "0c4f74204b1b41f8b94ae9aee304087e"

url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=0c4f74204b1b41f8b94ae9aee304087e"




response = requests.get(url)
content = response.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])

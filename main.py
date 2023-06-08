import requests
from send_mail import send_email

api_key = "0c4f74204b1b41f8b94ae9aee304087e"

topic = "wsj.com"

url = f"https://newsapi.org/v2/everything?domains={topic}&apiKey=0c4f74204b1b41f8b94ae9aee304087e&language=en"

response = requests.get(url)
content = response.json()

body = ""

for article in content["articles"][:5]:
    if article["title"] is not None:
        body = "Subject: Today's topic" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 3 * "\n"

body = body.encode("utf-8")
send_email(message=body)

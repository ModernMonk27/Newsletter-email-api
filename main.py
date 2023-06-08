import requests
from  send_mail import send_email

api_key = "0c4f74204b1b41f8b94ae9aee304087e"

url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=0c4f74204b1b41f8b94ae9aee304087e"




response = requests.get(url)
content = response.json()

body = ""

for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 3*"\n"


body = body.encode("utf-8")
send_email(message=body)




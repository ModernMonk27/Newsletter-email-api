import requests



url ="https://api.nasa.gov/planetary/apod?api_key=exUe7idAcrXfKf1EEgj0HbYyh5Vx9LQdU8Rl2v6J"

response = requests.get(url)

content = response.json()

print(content)
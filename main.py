import requests

response = requests.get("https://www.ceneo.pl/96570690#tab=reviews")
print(response.text)
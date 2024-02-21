import requests

url = "https://api-football-v1.p.rapidapi.com/v3/countries"

headers = {
	"X-RapidAPI-Key": "952272c7d3mshfc9fb6eb226c0c4p1ac5a6jsn1c31d9936615",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())
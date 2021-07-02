import requests

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"to_currency":"JPY","function":"CURRENCY_EXCHANGE_RATE","from_currency":"USD"}

headers = {
    'x-rapidapi-key': "2a9cdbe220msh52b5f56e5b1a596p1dc6dfjsnecc135e4c219",
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)

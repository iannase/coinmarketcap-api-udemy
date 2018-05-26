import json
import requests
from datetime import datetime

listings_url = 'https://api.coinmarketcap.com/v2/listings/'

request = requests.get(listings_url)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']

print()
for currency in data:
    rank = currency['id']
    name = currency['name']
    symbol = currency['symbol']
    print(str(rank) + ': ' + name + ' (' + symbol + ')')
print()

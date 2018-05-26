import json
import requests
from datetime import datetime

convert = 'USD'

global_url = 'https://api.coinmarketcap.com/v2/global/' + '?convert=' + convert

request = requests.get(global_url)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']
active_currencies = data['active_cryptocurrencies']
active_markets = data['active_markets']
bitcoin_percentage = data['bitcoin_percentage_of_market_cap']
last_updated_timestamp = data['last_updated']
global_cap = int(data['quotes']['USD']['total_market_cap'])
global_volume = int(data['quotes']['USD']['total_volume_24h'])

active_currencies_string = '{:,}'.format(active_currencies)
active_markets_string = '{:,}'.format(active_markets)
global_cap_string = '{:,}'.format(global_cap)
global_volume_string = '{:,}'.format(global_volume)

last_updated_string = datetime.fromtimestamp(last_updated_timestamp).strftime('%B %d, %Y at %I:%M%p')

print()
print('There are currently ' + active_currencies_string + ' active currencies and ' + active_markets_string + ' active markets.')
print('The global market cap is $' + global_cap_string + ' and the 24h volume is $' + global_volume_string + '.')
print('Bitcoin\'s market cap makes up ' + str(bitcoin_percentage) + '% of the global market cap.')
print()
print('This information was updated on ' + last_updated_string + '.')
print()

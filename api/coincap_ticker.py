import json
import requests
from datetime import datetime

ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array'

limit = 100
start = 1
sort = 'id'
convert = 'USD'

while True:
    choice = input('Do you want to enter custom parameters? (y/n): ')

    if choice == 'y':
        limit = input('Number of currencies limit (default 100): ')
        start = input('Currency starting on (default 1): ')
        sort = input('What would you like to sort on (default rank): ')

    ticker_url += '&limit=' + str(limit) + '&start=' + str(start) + '&sort=' + '&convert=' + convert

    request = requests.get(ticker_url)
    results = request.json()

    print(json.dumps(results, sort_keys=True, indent=4))

    data = results['data']

    print()
    for currency in data:
        rank = currency['rank']
        name = currency['name']
        symbol = currency['symbol']

        circulating_supply = int(currency['circulating_supply'])
        total_supply = int(currency['total_supply'])

        quotes = currency['quotes'][convert]
        market_cap = quotes['market_cap']
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']

        volume_string = '{:,}'.format(volume)
        market_cap_string = '{:,}'.format(market_cap)
        circulating_supply_string = '{:,}'.format(circulating_supply)
        total_supply_string = '{:,}'.format(total_supply)

        print(str(rank) + ': ' + name + ' (' + symbol + ')')
        print('Market cap: \t\t$' + market_cap_string)
        print('Price: \t\t\t$' + str(price))
        print('24h Volume: \t\t$' + str(volume) + '%')
        print('Hour change: \t\t' + str(hour_change) + '%')
        print('Day change: \t\t' + str(day_change) + '%')
        print('Week change: \t\t' + str(week_change) + '%')
        print('Circulating supply: \t' + circulating_supply_string)
        print('Total supply: \t\t' + total_supply_string)
        print('Percentage circulating: ' + str(int(circulating_supply / total_supply * 100)) + '%')
        print()
    print()

    choice = input('Again? (y/n): ')

    if choice == 'n':
        break

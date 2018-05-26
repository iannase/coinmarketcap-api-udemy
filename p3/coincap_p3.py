import json
import requests
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

convert = 'USD'

global_url = 'https://api.coinmarketcap.com/v2/global/' + '?convert=' + convert

request = requests.get(global_url)
results = request.json()

data = results['data']
global_cap = int(data['quotes']['USD']['total_market_cap'])
global_cap_string = '{:,}'.format(global_cap)

while True:
    print()
    print("CoinMarketCap Explorer Menu")
    print("The global market cap is $" + global_cap_string)
    print()
    print("1 - Top 100 sorted by rank")
    print("2 - Top 100 sorted by 24 hour percent change")
    print("3 - Top 100 sorted by 24 hour volume")
    print("0 - Exit")
    print()
    choice = input('What is your choice (1-3)?: ')

    ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array&sort='

    if choice == '1':
        ticker_url += 'rank'
    if choice == '2':
        ticker_url += 'percent_change_24h'
    if choice == '3':
        ticker_url += 'volume_24h'
    if choice == '0':
        break

    request = requests.get(ticker_url)
    results = request.json()

    # print(json.dumps(results, sort_keys=True, indent=4))

    data = results['data']

    table = PrettyTable(['Rank', 'Asset', 'Price', 'Market Cap', 'Volume', '1h', '24h', '7d'])

    print()
    for currency in data:
        rank = currency['rank']
        name = currency['name']
        symbol = currency['symbol']
        quotes = currency['quotes'][convert]
        market_cap = quotes['market_cap']
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']

        if hour_change is not None:
            if hour_change > 0:
                hour_change = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
            else:
                hour_change = Back.RED + str(hour_change) + '%' + Style.RESET_ALL

        if day_change is not None:
            if day_change > 0:
                day_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
            else:
                day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL

        if week_change is not None:
            if week_change > 0:
                week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
            else:
                week_change = Back.RED + str(week_change) + '%' + Style.RESET_ALL

        if volume is not None:
            volume_string = '{:,}'.format(volume)

        if market_cap is not None:
            market_cap_string = '{:,}'.format(market_cap)

        table.add_row([rank,
                       name + ' (' + symbol + ')',
                       '$' + str(price),
                       '$' + market_cap_string,
                       '$' + volume_string,
                       str(hour_change),
                       str(day_change),
                       str(week_change)])

        # print(str(rank) + ': ' + name + ' (' + symbol + ')')
        # print('Market cap: \t\t$' + market_cap_string)
        # print('Price: \t\t\t$' + str(price))
        # print('24h Volume: \t\t$' + str(volume) + '%')
        # print('Hour change: \t\t' + str(hour_change) + '%')
        # print('Day change: \t\t' + str(day_change) + '%')
        # print('Week change: \t\t' + str(week_change) + '%')
        # print('Circulating supply: \t' + circulating_supply_string)
        # print('Total supply: \t\t' + total_supply_string)
        # print('Percentage circulating: ' + str(int(circulating_supply / total_supply * 100)) + '%')
        # print()

    print()
    print(table)
    print()

    choice = input('Again? (y/n): ')

    if choice == 'n':
        break

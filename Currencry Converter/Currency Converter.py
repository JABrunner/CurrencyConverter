# import modules
from locale import currency
from urllib import response
from requests import get
from pprint import PrettyPrinter

#declare varibles for url to send info with API key
BASE_URL = "https://free.currconv.com/"
API_KEY = "040fcb2e8ff46fd349dd"

#construct printer
printer = PrettyPrinter()


#get currency information
def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']

    data = list(data.items())
    data.sort()

    return data

#print currency information
def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol", "")
        print(F"{_id} - {name} - {symbol}")

#get exchange rate from currencies
def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()


    #prevent app from printing nonexistant currencies
    if len(data) == 0:
        print('Invalid currencies.')
        return

    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")
    
    return rate

#convert currency exhange rates
def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)

    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount

def main():
    currencies = get_currencies()

    print("Welcome to the currencry converter!")
    print(" Choose 'List' to see the differ lists of different currencies")
    print("Choose 'Convert' to conver from one currency to another")
    print("Choose 'Rate' to get the exhange rate of two currencies")
    print()

    while True:
        command = input("Enter a command or Q to Quit: ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter base Currency ID:").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter 2nd Currency ID: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to conver to: ").upper()
            exchange_rate(currency1,currency2)
        else:
            print("Unrecognized command!")
main()

            


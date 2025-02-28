import requests
import sys
import json


def main():
    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit(1)
    elif len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)
        else:
            try:
                response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
                data = response.json()
                amount = n * data["bpi"]["USD"]["rate_float"]
                print(f"${amount:,.4f}")
            except requests.RequestException:
                print("Request failed!")
                sys.exit(1)

main()

# https://api.coindesk.com/v1/bpi/currentprice.json
import sys
import requests
import json

def main():
    number = validator()
    calculator(number)




def validator():
  # Verify Length of the input
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py INTEGER")

    # Try to convert the argv[1] to float
    try:
       number = float(sys.argv[1])
    except:
       sys.exit("Usage: python bitcoin.py INTEGER")

    return number

def calculator(n):
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = request.json()
    price = data["bpi"]["USD"]["rate_float"]
    value = price * n
    print(f"${value:,.4f}")

if __name__ == "__main__":
  main()
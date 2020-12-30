import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")
url = "https://www.iban.com/currency-codes"
first_country = ""
second_country = ""

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

req = requests.get(url)
bs = BeautifulSoup(req.text, 'html.parser')

table = bs.find('table', {"class": "table"})
lines = table.findAll('tr')[1:]

spans = []

for line in lines:
    tds = line.find_all("td")
    country = tds[0].text
    currency = tds[1].text
    code = tds[2].text
    if currency != "No universal currency":
        span = {
            "country": country,
            "currency": currency,
            "code": code
        }
        spans.append(span)
    else:
        pass

def get_number():
  try:
    a = int(input("#: "))
    if a > len(spans):
      print("Choose a number from the list.")
      get_number()
    else:
      span = spans[a]
      get_code = span['code']
      if get_code != "":
        return get_code
  except ValueError:
    print("That wasn't a number.")
    get_number()

def change():
    print(
        f"\nHow many {first_code} do you want to convert to {second_code}?\n")
    a = input()
    if a.isdigit() == True:
        html = requests.get(
            f"https://transferwise.com/gb/currency-converter/{first_code}-to-{second_code}-rate?amount={a}")
        bs = BeautifulSoup(html.text, 'html.parser')
        b = bs.find("form").find("input")["value"]
        c = float(a) * float(b)
        start = format_currency(a, first_code, locale="ko_KR")
        result = format_currency(c, second_code, locale="ko_KR")
        print(f"{start} is {result}")
    else:
        print("That wasn't a number")
        change()

def converter():
  global first_code, second_code
  print("\nWhere are you from? Choose a country by number.\n")
  first_code = get_number()
  print("\nNow choose another country.\n")
  second_code = get_number()
  change()

for i, span in enumerate(spans):
    print(f"#{i} {span['country']}")

print("Welcome to CurrencyConvert PRO 2000")
converter()

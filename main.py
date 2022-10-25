import json

from google_currency import convert

from_currency = str(input("Enter the currency you would like to convert to: ")).lower()

to_currency = str(input("Enter the currency you would live to convert from:")).lower()

amount = float(input("Enter the amount of your currency to be converted: "))

conversion = json.loads(convert(to_currency,from_currency,amount))

formatted_result = json.dumps(conversion, indent=4)

print(formatted_result)





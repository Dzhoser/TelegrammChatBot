import requests
import json
from config import keys

class ConversionException(Exception):
    pass

class CurrConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConversionException(f"Невозможно перевести одинаковые валюты {quote}")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f"Не удалось обработать валюту {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f"Не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except KeyError:
            raise ConversionException(f"Не удалось обработать количество {amount}")

        r = requests.get(f'https://api.apilayer.com/currency_data/live?source={quote_ticker}&currencies={base_ticker}&apikey=TPF7Gv7QHliY6k5qmI2zuPuNqbsPoLiL')

        totalbase = json.loads(r.content)['quotes'][f'{keys[quote]}{keys[base]}']

        return totalbase

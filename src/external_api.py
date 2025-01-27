import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv(".env")


def getting_converted_currency(currency: str, amount: float | int) -> list[dict[Any, Any] | dict[Any, Any]]:
    """Функция запрашивает настоящий курс стоимости валюты
    и конвертирует сумму операции в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB%2CUSD%2CEUR&base={currency}"
    headers = {"apikey": f'{os.getenv("API_LAYER_KEY")}'}
    response = requests.request("GET", url, headers=headers)
    exchange_rates_data = response.json()
    currencies_in_rubles = exchange_rates_data["rates"]["RUB"]
    converted_operation = amount * currencies_in_rubles
    return round(converted_operation, 2)

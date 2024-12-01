from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

my_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(my_dict))
print(sort_by_date(my_dict))


account_number_one = "2000236548846996"
account_number_two = "73654108430135874305"

print(get_mask_card_number(account_number_one))
print(get_mask_account(account_number_two))


account_number_two = "Счет 64686473678894779589"
account_number_one = "Visa Classic 6831982476737658"

print(mask_account_card(account_number_one))
print(mask_account_card(account_number_two))
print(get_date(datetime.now()))

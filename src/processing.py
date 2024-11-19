def filter_by_state(state_dict: list[dict[str, object]], state: str = "EXECUTED") -> list[dict[str, object]]:
    """Функция возвращает список словарей по значению ключа "state" = EXECUTED"""
    new_dict = []
    for dict_ in state_dict:
        if dict_["state"] == state:
            new_dict.append(dict_)
    return new_dict


def sort_by_date(users_dict: list, reverse_list_dict: bool = True) -> list:
    """Функция сортирует список словарей по убыванию (reverse_list_dict = True)"""
    sort_by_date_dict = sorted(users_dict, key=lambda item: item["date"], reverse=reverse_list_dict)
    return sort_by_date_dict


if __name__ == "__main__":
    my_dict = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(filter_by_state(my_dict))
    print(sort_by_date(my_dict))

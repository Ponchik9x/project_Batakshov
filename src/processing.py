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

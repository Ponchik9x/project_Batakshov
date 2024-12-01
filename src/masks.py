def get_mask_card_number(card_num: str) -> str:
    """Функция показывает первые 6 цифр и последние 4 цифры в блоке по 4 цифры,
    а остальные цифры заменяет на символ'*'"""
    return f"{card_num[0:4]} {card_num[4:6]}** **** {card_num[-4:]}"


def get_mask_account(card_num: str) -> str:
    """ "Функция заменяет все цифры символом '*' и возвращает последние 4 цифры"""
    return f" **{card_num[-4:]}"


if __name__ == "__main__":
    account_number_one = "2000236548846996"
    print(get_mask_card_number(account_number_one))
    account_number_two = "73654108430135874305"
    print(get_mask_account(account_number_two))

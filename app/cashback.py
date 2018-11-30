# Задача первая
def calculate_cashback(data):
    """
    >>> calculate_cashback(50000, 1)
    500.0
    >>> calculate_cashback(50000, 5)
    2500.0
    >>> calculate_cashback(50000, 30)
    15000.0
    """
    sum_of_buy = data[0]
    type_buy = data[1]
    cashback = (sum_of_buy * type_buy * 0.01) // 1
    return cashback


def sum_of_cashback(data):
    """
    >>> sum_of_cashback(3010, 1)
    'Кэшбэк сосятавляет 3000 рублей. Остаток свыше этой суммы сгорает.'
    >>> sum_of_cashback(3000, 1)
    3000
    >>> sum_of_cashback(3010, 5)
    'Кэшбэк сосятавляет 3000 рублей. Остаток свыше этой суммы сгорает.'
    >>> sum_of_cashback(6010, 30)
    'Кэшбэк сосятавляет 6000 рублей. Остаток свыше этой суммы переходит на следующий месяц.'
    """
    cashback = data[0]
    type_of_buy = data[1]

    if type_of_buy == 1 and cashback > 3000:
        return "Кэшбэк сосятавляет 3000 рублей. Остаток свыше этой суммы сгорает."
    elif cashback <= 3000:
        return cashback
    if type_of_buy == 5 and cashback > 3000:
        return "Кэшбэк сосятавляет 3000 рублей. Остаток свыше этой суммы сгорает."
    elif cashback <= 3000:
        return cashback
    if type_of_buy == 30 and cashback > 6000:
        return "Кэшбэк сосятавляет 6000 рублей. Остаток свыше этой суммы переходит на следующий месяц."
    elif cashback <= 6000:
        return cashback


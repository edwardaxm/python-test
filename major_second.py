# Задача вторая
def calculate_deposit(data):
    """
    >>> calculate_deposit(20_000, 10, 12)
    22000
    >>> calculate_deposit(150_000, 8, 60)
    210000
    >>> calculate_deposit(50_000, 8, 1)
    50340
    """
    sum_of_deposit = data[0]
    percentage_rate = data[1]
    term_of_placement = data[2]

    total = (sum_of_deposit * percentage_rate * term_of_placement) / 12 / 100 + sum_of_deposit
    return round(total)

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

    if term_of_placement == 1:
        total = (sum_of_deposit * percentage_rate * 31) / (365 * 100) + sum_of_deposit
        return round(total)
    if term_of_placement == 3:
        total = (sum_of_deposit * percentage_rate * 92) / (365 * 100) + sum_of_deposit
        return round(total)
    if term_of_placement == 6:
        total = (sum_of_deposit * percentage_rate * 182) / (365 * 100) + sum_of_deposit
        return round(total)
    if term_of_placement == 9:
        total = (sum_of_deposit * percentage_rate * 273) / (365 * 100) + sum_of_deposit
        return round(total)
    if term_of_placement == 12:
        total = (sum_of_deposit * percentage_rate * 365) / (365 * 100) + sum_of_deposit
        return round(total)
    if term_of_placement == 18:
        total = (sum_of_deposit * percentage_rate * 548) / (365 * 100) + sum_of_deposit
        return round(total)
    if term_of_placement == 24:
        total = (sum_of_deposit * percentage_rate * 730) / (365 * 100) + sum_of_deposit
        return round(total)
    if term_of_placement == 36:
        total = (sum_of_deposit * percentage_rate * 1095) / (365 * 100) + sum_of_deposit
        return round(total)
    if term_of_placement == 60:
        total = (sum_of_deposit * percentage_rate * 1825) / (365 * 100) + sum_of_deposit
        return round(total)

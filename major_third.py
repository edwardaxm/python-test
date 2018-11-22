# сумма ежемесячного платежа
def monthly_payment(data):
    """
    >>> monthly_payment(1_550_000, 15, 34)
    56240
    """
    credit = data[0]
    percent = data[1]
    term_of_credit = data[2]
    i = 0.01 * percent / 12
    payment = credit * ((i *((1 + i) ** term_of_credit))/(((1 + i) ** term_of_credit) -1))
    return round(payment)

# выплаты за весь срок кредита
def total_payment(data):
    """
    >>> total_payment(56_240, 34)
    1912160
    """
    monthly_payment = data[0]
    term_of_credit = data[1]
    total = monthly_payment * term_of_credit
    return total

# переплата по кредиту
def overpayment_on_loan(data):
    """
    >>> overpayment_on_loan(1_912_160, 1_550_000)
    362160
    """
    total = data[0]
    credit = data[1]
    overpayment = total - credit
    return overpayment

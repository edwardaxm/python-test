import pytest

from app import cashback


# Тесты к первой задаче
def test_first_task_1():
    data = 50000, 1
    actual = cashback.calculate_cashback(data)
    assert 500 == actual


def test_first_task_2():
    data = 50000, 5
    actual = cashback.calculate_cashback(data)
    assert 2500 == actual


def test_first_task_3():
    data = 50000, 30
    actual = cashback.calculate_cashback(data)
    assert 15000 == actual


def test_first_task_4():
    data = 3010, 1
    actual = cashback.sum_of_cashback(data)
    assert 'Кэшбэк сосятавляет 3000 рублей. Остаток свыше этой суммы сгорает.' == actual


def test_first_task_5():
    data = 3000, 1
    actual = cashback.sum_of_cashback(data)
    assert 3000 == actual


def test_first_task_6():
    data = 3010, 5
    actual = cashback.sum_of_cashback(data)
    assert 'Кэшбэк сосятавляет 3000 рублей. Остаток свыше этой суммы сгорает.' == actual


def test_first_task_7():
    data = 3000, 5
    actual = cashback.sum_of_cashback(data)
    assert 3000 == actual


def test_first_task_8():
    data = 6010, 30
    actual = cashback.sum_of_cashback(data)
    assert 'Кэшбэк сосятавляет 6000 рублей. Остаток свыше этой суммы переходит на следующий месяц.' == actual


def test_first_task_9():
    data = 6000, 30
    actual = cashback.sum_of_cashback(data)
    assert 6000 == actual

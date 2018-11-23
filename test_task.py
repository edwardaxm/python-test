import pytest

import major
import major_second
import major_third


# Тесты к первой задаче
def test_first_task_1():
    data = 50000, 1
    actual = major.calculate_cashback(data)
    assert 500 == actual


def test_first_task_2():
    data = 50000, 5
    actual = major.calculate_cashback(data)
    assert 2500 == actual


def test_first_task_3():
    data = 50000, 30
    actual = major.calculate_cashback(data)
    assert 15000 == actual


def test_first_task_4():
    data = 3010, 1
    actual = major.sum_of_cashback(data)
    assert 'Кэшбэк сосятавляет 3000 рублей. Остаток свыше этой суммы сгорает.' == actual


def test_first_task_5():
    data = 3000, 1
    actual = major.sum_of_cashback(data)
    assert 3000 == actual


def test_first_task_6():
    data = 3010, 5
    actual = major.sum_of_cashback(data)
    assert 'Кэшбэк сосятавляет 3000 рублей. Остаток свыше этой суммы сгорает.' == actual


def test_first_task_7():
    data = 3000, 5
    actual = major.sum_of_cashback(data)
    assert 3000 == actual


def test_first_task_8():
    data = 6010, 30
    actual = major.sum_of_cashback(data)
    assert 'Кэшбэк сосятавляет 6000 рублей. Остаток свыше этой суммы переходит на следующий месяц.' == actual


def test_first_task_9():
    data = 6000, 30
    actual = major.sum_of_cashback(data)
    assert 6000 == actual


# Тесты ко второй задаче

def test_second_task_1():
    data = 20_000, 10, 12
    actual = major_second.calculate_deposit(data)
    assert 22000 == actual


def test_second_task_2():
    data = 150_000, 8, 60
    actual = major_second.calculate_deposit(data)
    assert 210000 == actual


def test_second_task_3():
    data = 50_000, 8, 1
    actual = major_second.calculate_deposit(data)
    assert 50333 == actual


@pytest.mark.xfail(strict=True)
def test_second_task_4():
    data = 50_000, 8, 1
    actual = major_second.calculate_deposit(data)
    assert 503490 == actual


# Тесты к третей задаче

def test_third_task_1():
    data = 1_550_000, 15, 34
    actual = major_third.monthly_payment(data)
    assert 56240 == actual


def test_third_task_2():
    data = 56_240, 34
    actual = major_third.total_payment(data)
    assert 1912160 == actual


def test_third_task_3():
    data = 1_912_160, 1_550_000
    actual = major_third.overpayment_on_loan(data)
    assert 362160 == actual


@pytest.mark.xfail(strict=True)
def test_third_task_4():
    data = 1_912_160, 1_550_000
    actual = major_third.overpayment_on_loan(data)
    assert 3621690 == actual


@pytest.mark.xfail(strict=True)
def test_third_task_5():
    data = 1_912_160, 1_550_000
    actual = major_third.overpayment_on_loan(data)
    assert 1 == actual

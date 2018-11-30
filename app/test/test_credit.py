import pytest

from app import credit

# Тесты к третей задаче

def test_third_task_1():
    data = 1_550_000, 15, 34
    actual = credit.monthly_payment(data)
    assert 56240 == actual


def test_third_task_2():
    data = 56_240, 34
    actual = credit.total_payment(data)
    assert 1912160 == actual


def test_third_task_3():
    data = 1_912_160, 1_550_000
    actual = credit.overpayment_on_loan(data)
    assert 362160 == actual


@pytest.mark.xfail(strict=True)
def test_third_task_4():
    data = 1_912_160, 1_550_000
    actual = credit.overpayment_on_loan(data)
    assert 3621690 == actual


@pytest.mark.xfail(strict=True)
def test_third_task_5():
    data = 1_912_160, 1_550_000
    actual = credit.overpayment_on_loan(data)
    assert 1 == actual

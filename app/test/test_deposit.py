import pytest

from app import deposit

# Тесты ко второй задаче
def test_second_task_1():
    data = 20_000, 10, 12
    actual = deposit.calculate_deposit(data)
    assert 22000 == actual


def test_second_task_2():
    data = 150_000, 8, 60
    actual = deposit.calculate_deposit(data)
    assert 210000 == actual


def test_second_task_3():
    data = 50_000, 8, 1
    actual = deposit.calculate_deposit(data)
    assert 50333 == actual


@pytest.mark.xfail(strict=True)
def test_second_task_4():
    data = 50_000, 8, 1
    actual = deposit.calculate_deposit(data)
    assert 503490 == actual

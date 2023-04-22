import pytest
from account import *


def test_init():

    acc1 = account("Val")
    assert acc1.getname() == "Val"
    assert acc1.getbalance() == 0


def test_deposit():

    acc1 = account("Val")
    acc1.deposit(20)
    assert acc1.getbalance() == 20


def test_withdraw():

    acc1 = account("Val")
    acc1.deposit(10)
    acc1.withdraw(2)
    assert acc1.getbalance() == 8
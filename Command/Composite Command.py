from abc import ABC
from enum import Enum
import unittest


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, balance = {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrawn {amount}, balance = {self.balance}")
            return True
        return False

    def __str__(self):
        return f"Balance = {self.balance}"


class Command(ABC):
    def __init__(self):
        self.success = False

    def invoke(self):
        pass

    def undo(self):
        pass


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account, action, amount):
        super().__init__()
        self.amount = amount
        self.action = action
        self.account = account

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


class CompositeBankAccountCommand(Command, list):
    def __init__(self, items=[]):
        super().__init__()
        if items is None:
            items = []
        for i in items:
            self.append(i)

    def invoke(self):
        for x in self:
            x.invoke()

    def undo(self):
        for x in reversed(self):
            x.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_acc, to_acc, amount):
        super().__init__(
            [
                BankAccountCommand(from_acc, BankAccountCommand.Action.WITHDRAW, amount),
                BankAccountCommand(to_acc, BankAccountCommand.Action.DEPOSIT, amount)
            ]
        )

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False

        self.success =  ok


class TestSuite(unittest.TestCase):
    # def test_composite_deposit(self):
    #     ba = BankAccount()
    #     deposit1 = BankAccountCommand(
    #         ba, BankAccountCommand.Action.DEPOSIT, 100
    #     )
    #     deposit2 = BankAccountCommand(
    #         ba, BankAccountCommand.Action.DEPOSIT, 100
    #     )
    #     composite = CompositeBankAccountCommand(
    #         [deposit1,deposit2]
    #     )
    #     composite.invoke()
    #     print(ba)
    #     composite.undo()
    #     print(ba)

    # def test_transfer_fail(self):
    #     ba1 = BankAccount(100)
    #     ba2 = BankAccount()
    #     amount = 1000
    #     wc = BankAccountCommand(
    #         ba1, BankAccountCommand.Action.WITHDRAW, amount
    #     )
    #     dc = BankAccountCommand(
    #         ba2, BankAccountCommand.Action.DEPOSIT, amount
    #     )
    #     transfer = CompositeBankAccountCommand([wc, dc])
    #     transfer.invoke()
    #     print(f"ba1: {ba1}, ba2: {ba2}")
    #     transfer.undo()
    #     print(f"ba1: {ba1}, ba2: {ba2}")

    def test_better_transfer(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        amount = 1000
        transfer = MoneyTransferCommand(ba1, ba2, amount)
        transfer.invoke()
        print(f"ba1: {ba1}, ba2: {ba2}")
        transfer.undo()
        print(f"ba1: {ba1}, ba2: {ba2}")


if __name__ == "__main__":
    unittest.main()

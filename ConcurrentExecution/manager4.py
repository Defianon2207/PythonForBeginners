from multiprocessing import Process
from multiprocessing.managers import BaseManager


class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            return False

        self._balance -= amount
        return True

    def get_balance(self):
        return self._balance


class AccountManager(BaseManager):
    pass


AccountManager.register(
    "BankAccount",
    callable=BankAccount
)


def add_money(account):
    for _ in range(1_000):
        account.deposit(10)


if __name__ == "__main__":
    with AccountManager() as manager:
        account = manager.BankAccount(1_000)

        processes = [
            Process(target=add_money, args=(account,))
            for _ in range(4)
        ]

        for process in processes:
            process.start()

        for process in processes:
            process.join()

        print(account.get_balance())
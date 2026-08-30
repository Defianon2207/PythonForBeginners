from multiprocessing import Process
from multiprocessing.managers import BaseManager


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False

        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance


# Create a customized manager class
class BankManager(BaseManager):
    pass


# Register BankAccount with BankManager
BankManager.register(
    "BankAccount",
    callable=BankAccount
)


def worker(account, amount):
    account.deposit(amount)


if __name__ == "__main__":
    with BankManager() as manager:
        # The actual BankAccount lives in the manager process.
        # This variable contains a proxy.
        account = manager.BankAccount(1_000)

        processes = [
            Process(target=worker, args=(account, 100)),
            Process(target=worker, args=(account, 200)),
            Process(target=worker, args=(account, 300)),
        ]

        for process in processes:
            process.start()

        for process in processes:
            process.join()

        print("Final balance:", account.get_balance())
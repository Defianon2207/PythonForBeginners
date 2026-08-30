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


class BankManager(BaseManager):
    pass


BankManager.register(
    "BankAccount",
    callable=BankAccount,
    exposed=(
        "deposit",
        "withdraw",
        "get_balance",
    )
)


def deposit_money(account, amount):
    account.deposit(amount)


def withdraw_money(account, amount):
    successful = account.withdraw(amount)

    print(
        f"Withdraw ₹{amount}:",
        "successful" if successful else "failed"
    )


if __name__ == "__main__":
    with BankManager() as manager:
        account = manager.BankAccount(1_000)

        processes = [
            Process(
                target=deposit_money,
                args=(account, 500)
            ),
            Process(
                target=withdraw_money,
                args=(account, 200)
            ),
        ]

        for process in processes:
            process.start()

        for process in processes:
            process.join()

        print("Final balance:", account.get_balance())
import threading

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

        # Reentrant lock
        self.lock = threading.RLock()

    def add_transaction(self, message):
        # Same thread acquires the same lock again
        with self.lock:
            self.transactions.append(message)
            print("Transaction recorded:", message)

    def deposit(self, amount):
        # First acquisition
        with self.lock:
            print("Deposit acquired the lock")

            self.balance += amount

            # This method acquires the same lock again
            self.add_transaction(f"Deposited ₹{amount}")

            print("Deposit completed")


account = BankAccount(1000)

account.deposit(500)

print("Balance:", account.balance)
print("Transactions:", account.transactions)


class Configuration:
    def __init__(self):
        self.settings = {
            "theme": "dark",
            "language": "English"
        }

        self.lock = threading.RLock()

    def set_value(self, key, value):
        with self.lock:
            print(f"Setting {key} to {value}")
            self.settings[key] = value

    def reset(self):
        with self.lock:
            print("Reset started")

            # These methods acquire the same lock again
            self.set_value("theme", "light")
            self.set_value("language", "English")

            print("Reset completed")


config = Configuration()
config.reset()

print(config.settings)
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from threading import Lock
import time
import random


class Inventory:
    def __init__(self):
        self._stock = {
            "laptop": 5,
            "phone": 10,
            "tablet": 3,
        }

        # Protects stock inside the manager process
        self._lock = Lock()

    def reserve(self, product, quantity):
        with self._lock:
            available = self._stock.get(product, 0)

            if available < quantity:
                return {
                    "success": False,
                    "product": product,
                    "requested": quantity,
                    "available": available,
                }

            self._stock[product] -= quantity

            return {
                "success": True,
                "product": product,
                "reserved": quantity,
                "remaining": self._stock[product],
            }

    def restock(self, product, quantity):
        with self._lock:
            self._stock[product] = (
                self._stock.get(product, 0) + quantity
            )

            return self._stock[product]

    def get_stock(self):
        with self._lock:
            # Return a copy so callers cannot modify stock directly
            return self._stock.copy()


class StoreManager(BaseManager):
    pass


StoreManager.register(
    "Inventory",
    callable=Inventory,
    exposed=(
        "reserve",
        "restock",
        "get_stock",
    )
)


def process_order(inventory, order_id, product, quantity):
    time.sleep(random.uniform(0.1, 0.5))

    result = inventory.reserve(product, quantity)

    if result["success"]:
        print(
            f"Order {order_id}: reserved "
            f"{quantity} {product}(s). "
            f"Remaining: {result['remaining']}"
        )
    else:
        print(
            f"Order {order_id}: failed. "
            f"Requested {quantity} {product}(s), "
            f"but only {result['available']} available."
        )


if __name__ == "__main__":
    with StoreManager() as manager:
        inventory = manager.Inventory()

        orders = [
            ("ORD-101", "laptop", 2),
            ("ORD-102", "laptop", 2),
            ("ORD-103", "laptop", 2),
            ("ORD-104", "phone", 4),
            ("ORD-105", "tablet", 2),
        ]

        processes = [
            Process(
                target=process_order,
                args=(inventory, order_id, product, quantity)
            )
            for order_id, product, quantity in orders
        ]

        for process in processes:
            process.start()

        for process in processes:
            process.join()

        print("\nFinal inventory:", inventory.get_stock())
from multiprocessing.managers import BaseManager
from threading import Lock


class Inventory:
    def __init__(self):
        self._stock = {
            "laptop": 10,
            "phone": 20,
            "tablet": 5,
        }
        self._lock = Lock()

    def reserve(self, product, quantity):
        with self._lock:
            available = self._stock.get(product, 0)

            if available < quantity:
                return {
                    "success": False,
                    "available": available,
                }

            self._stock[product] -= quantity

            return {
                "success": True,
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
            return self._stock.copy()


# One inventory shared by all connected clients
shared_inventory = Inventory()


def get_inventory():
    return shared_inventory


class StoreManager(BaseManager):
    pass


StoreManager.register(
    "get_inventory",
    callable=get_inventory,
    exposed=("reserve", "restock", "get_stock")
)


if __name__ == "__main__":
    manager = StoreManager(
        address=("0.0.0.0", 50000),
        authkey=b"store-secret"
    )

    server = manager.get_server()

    print("Inventory server is running")
    print("Address:", server.address)

    server.serve_forever()
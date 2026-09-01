from multiprocessing.managers import BaseManager


class StoreManager(BaseManager):
    pass


# Client registers the name but not the callable
StoreManager.register("get_inventory")


if __name__ == "__main__":
    manager = StoreManager(
        address=("127.0.0.1", 50000),
        authkey=b"store-secret"
    )

    manager.connect()

    inventory = manager.get_inventory()

    print("Current stock:", inventory.get_stock())

    result = inventory.reserve("laptop", 3)

    if result["success"]:
        print(
            "Order successful.",
            "Remaining laptops:",
            result["remaining"]
        )
    else:
        print(
            "Order failed.",
            "Available laptops:",
            result["available"]
        )

    print("Updated stock:", inventory.get_stock())
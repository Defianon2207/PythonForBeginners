import asyncio

balance = 1_000


async def withdraw(name, amount, lock):
    global balance

    async with lock:
        print(f"{name} acquired the lock")

        if balance >= amount:
            current_balance = balance

            # Simulate waiting for a database or network operation.
            await asyncio.sleep(1)

            balance = current_balance - amount
            print(f"{name} withdrew ₹{amount}")
        else:
            print(f"{name}: insufficient balance")

        print(f"{name} released the lock")


async def main():
    lock = asyncio.Lock()

    await asyncio.gather(
        withdraw("Rahul", 700, lock),
        withdraw("Amit", 700, lock),
    )
l   ock = asyncio.Lock()

    print(lock.locked())  # False

    await lock.acquire()
    print(lock.locked())  # True

    lock.release()
    print(lock.locked())  # False

    print("Final balance:", balance)


asyncio.run(main())
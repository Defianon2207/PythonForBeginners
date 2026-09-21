import asyncio
import threading
import time


# Imagine this belongs to an older payment SDK.
# It reports the result through a callback.
def start_payment(amount, on_complete):
    def process_payment():
        print(f"Processing payment of ₹{amount}...")
        time.sleep(2)

        # Payment gateway calls our callback later
        on_complete({
            "status": "success",
            "transaction_id": "TXN-48291",
        })

    threading.Thread(target=process_payment).start()


async def make_payment(amount):
    loop = asyncio.get_running_loop()

    # Represents a result that will become available later
    future = loop.create_future()

    def payment_completed(result):
        # This callback runs in the payment SDK's worker thread,
        # so communicate with the event loop safely.
        loop.call_soon_threadsafe(
            future.set_result,
            result,
        )

    start_payment(amount, payment_completed)

    # Suspend this coroutine until future.set_result() is called
    result = await future

    return result


async def main():
    print("Starting payment")

    result = await make_payment(1500)

    print("Payment status:", result["status"])
    print("Transaction ID:", result["transaction_id"])


asyncio.run(main())
import asyncio
from contextvars import ContextVar

request_id = ContextVar("request_id", default="NO-REQUEST")


def log(message):
    print(f"[{request_id.get()}] {message}")


async def validate_order():
    log("Validating order")
    await asyncio.sleep(0.2)


async def charge_customer():
    log("Charging customer")
    await asyncio.sleep(0.2)


async def process_order(order_id):
    with request_id.set(f"REQ-{order_id}"):
        log("Request started")

        await validate_order()
        await charge_customer()

        log("Request completed")


async def main():
    await asyncio.gather(
        process_order(101),
        process_order(102),
        process_order(103),
    )


asyncio.run(main())
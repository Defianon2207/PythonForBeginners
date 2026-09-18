import asyncio


async def calculate():
    print("Calculation started")
    await asyncio.sleep(2)
    print("Calculation finished")
    return 10 + 20


loop = asyncio.new_event_loop()

try:
    result = loop.run_until_complete(calculate())
    print("Result:", result)
finally:
    loop.close()
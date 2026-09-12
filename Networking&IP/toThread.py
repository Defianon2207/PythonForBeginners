import asyncio
import time

def blocking_operation():
    print("Blocking operation started")
    time.sleep(3)
    print("Blocking operation completed")
    return "Success"

async def show_messages():
    for number in range(3):
        print(f"Async message {number}")
        await asyncio.sleep(1)

async def main():
    result, _ = await asyncio.gather(
        asyncio.to_thread(blocking_operation),
        show_messages(),
    )

    print("Result:", result)

asyncio.run(main())
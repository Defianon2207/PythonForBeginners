#Repeated coroutine with run_forever()
import asyncio


async def heartbeat():
    count = 1

    while True:
        print(f"Heartbeat {count}")
        count += 1
        await asyncio.sleep(1)


loop = asyncio.new_event_loop()

try:
    task = loop.create_task(heartbeat())

    loop.call_later(4, loop.stop)

    loop.run_forever()
finally:
    task.cancel()
    loop.run_until_complete(
        asyncio.gather(task, return_exceptions=True)
    )
    loop.close()
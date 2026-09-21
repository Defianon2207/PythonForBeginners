import asyncio


async def main():
    loop = asyncio.get_running_loop()

    future = loop.create_future()

    def deliver_result():
        print("Providing the result")
        future.set_result(100)

    loop.call_later(2, deliver_result)

    print("Waiting...")
    result = await future

    print("Received:", result)


asyncio.run(main())
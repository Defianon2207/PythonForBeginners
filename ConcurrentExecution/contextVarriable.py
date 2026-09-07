import asyncio

current_user = None


async def process_request(user):
    global current_user

    current_user = user

    await asyncio.sleep(1)

    print(f"Processing request for {current_user}")


async def main():
    await asyncio.gather(
        process_request("Rahul"),
        process_request("Amit"),
    )


asyncio.run(main())
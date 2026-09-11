import asyncio

async def operation():
    print("Coroutine started")
    return 42

async def main():
    loop = asyncio.get_running_loop()
    loop.set_task_factory(asyncio.eager_task_factory)

    print("Before create_task")

    task = asyncio.create_task(operation())

    print("After create_task")

    result = await task
    print("Result:", result)

asyncio.run(main())
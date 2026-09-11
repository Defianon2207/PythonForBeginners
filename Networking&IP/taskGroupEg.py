import asyncio

async def download(name, seconds):
    print(f"Starting {name}")
    await asyncio.sleep(seconds)
    print(f"Finished {name}")
    return f"{name} downloaded"

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(download("File A", 3))
        task2 = tg.create_task(download("File B", 2))
        task3 = tg.create_task(download("File C", 1))

        print("All tasks have been created")

    # TaskGroup waits for every task before reaching this point.
    print("TaskGroup completed")

    print(task1.result())
    print(task2.result())
    print(task3.result())

asyncio.run(main())
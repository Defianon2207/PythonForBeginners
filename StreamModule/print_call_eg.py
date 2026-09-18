import asyncio


async def test():
    asyncio.print_call_graph()


async def main():
    async with asyncio.TaskGroup() as group:
        group.create_task(test(), name="test")


asyncio.run(main())
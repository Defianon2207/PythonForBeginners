import asyncio

def logging_factory(loop,coro,**kwargs):
    print("Creating Task", kwargs.get("name"))
    return asyncio.Task(
        coro,
        loop=loop,
        **kwargs,
    )


async def calculate():
    await asyncio.sleep(1)
    return 42


async def main():
    loop = asyncio.get_running_loop()

    previous_factory= loop.get_task_factory()
    print("Previous factory:", previous_factory)

    loop.set_task_factory(logging_factory)

    print("Custom factory active:",
    loop.get_task_factory() is logging_factory,
    )

    try:
        task = loop.create_task(
            calculate(),
            name = "calculation"
        )
        print("Result:", await task)
    finally:
        loop.set_task_factory(previous_factory)
    print("Factory restored:", loop.get_task_factory())


asyncio.run(main())
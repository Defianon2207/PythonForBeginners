import asyncio
from contextvars import ContextVar, copy_context


request_id = ContextVar("request_id")


async def main():
    loop = asyncio.get_running_loop()

    request_id.set("request-A")
    loop.call_soon(
        lambda: print("Default context:", request_id.get())
    )

    custom_context = copy_context()
    custom_context.run(request_id.set, "request-B")

    loop.call_soon(
        lambda: print("Custom context:", request_id.get()),
        context=custom_context,
    )

    await asyncio.sleep(0)


asyncio.run(main())
import asyncio


def new_callback():
    print("New callback executed")


def first_callback(loop):
    print("First callback")

    loop.call_soon(new_callback)
    loop.stop()


loop = asyncio.new_event_loop()

try:
    loop.call_soon(first_callback)

    print("First run:")
    loop.run_forever()

    print("Second run:")
    loop.call_soon(loop.stop)
    loop.run_forever()
    
finally:
    loop.close()
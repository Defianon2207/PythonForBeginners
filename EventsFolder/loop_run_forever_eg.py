import asyncio


def say_hello():
    print("Hello")


def stop_loop(loop):
    print("Stopping the loop")
    loop.stop()


loop = asyncio.new_event_loop()

try:
    loop.call_soon(say_hello)
    loop.call_later(2, stop_loop, loop)

    print("Starting the loop")
    loop.run_forever()
    print("run_forever() returned")
finally:
    loop.close()
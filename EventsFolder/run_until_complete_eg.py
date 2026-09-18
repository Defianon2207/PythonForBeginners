import asyncio


async def calculate():
    print("Calculation started")
    await asyncio.sleep(2)
    print("Calculation finished")
    return 10 + 20


loop = asyncio.new_event_loop()

try:
    result = loop.run_until_complete(calculate())
    print("Result:", result)
finally:
    loop.close()



# Refer this as well Normally, a task should be created while its target loop is current:

# import asyncio


# async def download():
#     await asyncio.sleep(1)
#     return "file downloaded"


# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)

# try:
#     task = loop.create_task(download())

#     result = loop.run_until_complete(task)

#     print(result)
# finally:
    loop.close()
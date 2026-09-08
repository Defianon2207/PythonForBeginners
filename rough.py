import asyncio

async def returnNumber():
    await asyncio.sleep(3)
    return 2
result = asyncio.run(
        returnNumber())

print(f"{result}")


# async def fileDownloader(name,time):
#     print(f"Downloading, {name}")
#     await asyncio.sleep(time)
#     print(f"Download complete after {time} seconds")


# async def main():
#     await asyncio.gather(
#         fileDownloader("Rahul",3),
#         fileDownloader("Kanchan",1)
#     )

# asyncio.run(main())
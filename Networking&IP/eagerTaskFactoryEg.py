import asyncio

cache = {
    "BTC": 100_000
}

async def fetch_price(symbol):
    if symbol in cache:
        print(f"{symbol}: found in cache")
        return cache[symbol]

    print(f"{symbol}: requesting from API")
    await asyncio.sleep(2)

    price = 5_000
    cache[symbol] = price
    return price

async def main():
    loop = asyncio.get_running_loop()
    loop.set_task_factory(asyncio.eager_task_factory)

    print("Creating BTC task")
    btc_task = asyncio.create_task(fetch_price("BTC"))
    print("BTC task created")

    print()

    print("Creating ETH task")
    eth_task = asyncio.create_task(fetch_price("ETH"))
    print("ETH task created")

    btc_price, eth_price = await asyncio.gather(
        btc_task,
        eth_task,
    )

    print("BTC:", btc_price)
    print("ETH:", eth_price)

asyncio.run(main())
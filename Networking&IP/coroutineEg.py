import asyncio

#A coroutine is a Python function that can pause while waiting, allow other work to run,
# and later resume from the same point.

# 1. Define a coroutine function using 'async def'
async def fetch_data(source_id: int, delay: int):
    print(f"[Source {source_id}] Starting fetch...")
    
    # 'await' pauses execution here and yields control back to the event loop
    await asyncio.sleep(delay)  # Simulates an asynchronous I/O operation (e.g., API call)
    
    print(f"[Source {source_id}] Fetch complete!")
    return {"source": source_id, "data": "Sample Payload"}

async def get_number():
    return 42


# Running multiple coroutine simulataneously
async def download(name,seconds):
    print(f"Starting {name}")
    await asyncio.sleep(seconds)
    print(f"Finished {name}")
    return name

async def main():
    # Calling an async function creates a coroutine object; it doesn't run it immediately.
    print("Program started.")
    
    # Executing a single coroutine using 'await'
    result = await fetch_data(1, 2)
    print(f"Received result: {result}\n")
    coroutine_object = get_number()
    # print("Co-routine",coroutine_object)
    result = await coroutine_object
    print("result",result)

# Entry point to run the asynchronous event loop
if __name__ == "__main__":
    asyncio.run(main())
    
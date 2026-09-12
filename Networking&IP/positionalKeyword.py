import asyncio
import time

def save_file(filename, content, *, overwrite=False):
    print(f"Saving {filename}")
    print(f"Content: {content}")
    print(f"Overwrite: {overwrite}")

    time.sleep(2)
    return len(content)

async def main():
    characters_written = await asyncio.to_thread(
        save_file,
        "report.txt",
        "Asyncio tutorial",
        overwrite=True,
    )

    print("Characters written:", characters_written)

asyncio.run(main())
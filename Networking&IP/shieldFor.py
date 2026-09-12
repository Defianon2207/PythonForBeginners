import asyncio

async def save_report():
    print("Saving report...")
    await asyncio.sleep(4)
    print("Report saved")
    return "report.pdf"

async def main():
    task = asyncio.create_task(save_report())

    try:
        result = await asyncio.wait_for(
            asyncio.shield(task),
            timeout=2,
        )
        print(result)

    except TimeoutError:
        print("Stopped waiting, but report is still being saved")

    # The task was protected from cancellation.
    result = await task
    print("Final result:", result)

asyncio.run(main())
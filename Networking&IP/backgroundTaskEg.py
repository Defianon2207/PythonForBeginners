import asyncio

background_tasks = set()


async def send_notification(user_id):
    print(f"Sending notification to user {user_id}....")
    await asyncio.sleep()
    print(f"Notification sent to user {user_id}")

    async def main():
        for user_id in range(1,6):
            
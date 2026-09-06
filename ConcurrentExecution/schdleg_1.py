import sched
import time

scheduler = sched.scheduler()


def remind(message):
    print(
        f"[{time.strftime('%H:%M:%S')}] "
        f"Reminder: {message}"
    )


scheduler.enter(
    2,
    1,
    remind,
    argument=("Check the server logs",)
)

scheduler.enter(
    5,
    1,
    remind,
    argument=("Take a short break",)
)

scheduler.enter(
    8,
    1,
    remind,
    argument=("Review the deployment",)
)

print("Reminder service started")
scheduler.run()
print("No reminders remaining")
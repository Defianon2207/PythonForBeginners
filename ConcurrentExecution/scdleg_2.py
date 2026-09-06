import sched
import time

scheduler = sched.scheduler()


def generate_balance_report(account_name, balance):
    current_time = time.strftime("%H:%M:%S")

    print(f"\nReport generated at {current_time}")
    print(f"Account: {account_name}")
    print(f"Balance: ₹{balance:,}")


print("Scheduler started at:", time.strftime("%H:%M:%S"))

scheduler.enter(
    delay=3,
    priority=1,
    action=generate_balance_report,
    argument=("Business Account", 250_000)
)

scheduler.enter(
    delay=5,
    priority=1,
    action=generate_balance_report,
    argument=("Savings Account", 500_000)
)

scheduler.run()

print("\nAll reports generated")
import sched
import time

scheduler = sched.scheduler()


def say_hello():
    print("Hello! Time:", time.strftime("%H:%M:%S"))


print("Scheduling at:", time.strftime("%H:%M:%S"))

scheduler.enter(
    delay=3,
    priority=1,
    action=say_hello
)

scheduler.run()

print("Scheduler finished")
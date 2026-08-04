import threading
import time
import random

# The game requires all three players.
barrier = threading.Barrier(3)


def player(name):
    loading_time = random.randint(1, 4)

    print(f"{name}: Loading game...")
    time.sleep(loading_time)
    print(f"{name}: Ready")

    # Wait until all three players reach this point.
    barrier.wait()

    print(f"{name}: Game started!")


threads = [
    threading.Thread(target=player, args=(f"Player {i}",))
    for i in range(1, 4)
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
# Create a Python program using multiprocessing that:

# Creates a shared integer using multiprocessing.Value, initially set to 0.
# Starts 5 processes.
# Each process increments the shared value 1,000 times.
# Prevents race conditions using the shared value’s lock.
# Waits for all processes to finish.
# Prints the final value.

from multiprocessing import Process, Pool
import multiprocessing

#This is the number which will be used by the multiprocessor
number = 0

def 

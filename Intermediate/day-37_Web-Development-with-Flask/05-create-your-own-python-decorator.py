# Objective Create your own decorator function to measure the amount of seconds that a function takes to execute. 
# 
# Expected Output
#
# 1695050908.1985211
# fast_function run speed: 0.33974480628967285s
# slow_function run speed: 2.9590742588043213s
#
# Calculating Time
# 
# time.time() will return the current time in seconds since January 1, 1970, 00:00:00.
#
# Try running the starting code to see the current time printed. 
# If you run the code after a while, you'll see a new time printed.
# e.g. first run:  1598524371.736911
# second run:  1598524436.357875 
# The time difference = second run - first run  64.62096405029297  (approx 1 minute) 
#
# Given the above information, complete the code exercise by printing out the time it takes to run the fast_function() vs the slow_function().

import time
 
def speed_calc_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time - start_time}s")
        return result
    return wrapper
 
@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
 
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i
 
fast_function()
slow_function()

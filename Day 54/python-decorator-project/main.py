import time

def speed_calc_decorator(function):
    def time_and_report():
        start = time.time()
        function()
        stop = time.time()
        time_taken = stop - start
        print(f"{function.__name__} run speed: {time_taken}s")
    return time_and_report

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

# Estimated time for 10.000.000.000 executions of counting sort is about 30hrs on my desktop computer. Based on timing 1.000.000 executions.
# Don't know how to estimate time for quick sorting big numbers once.

import time
from random import randint

# A little decorator to help us time the function execution
def timing(f):
    def wrap(*args):
        start_time = time.time()
        ret = f(*args)
        finish_time = time.time()
        print '%s function took %f ms' % (f.func_name, (finish_time-start_time)*1000.0)
        return ret
    return wrap

def counting_sort(array, max_value):
    count = [0] * max_value
    output = [0] * len(array)

    for num in array:
        count[num] += 1

    total = 0
    for i in range(max_value):
        oldCount = count[i]
        count[i] = total
        total += oldCount

    for num in array:
        output[count[num]] = num
        count[num] += 1

    return output

def quick_sort(array):
    if not array:
        return []

    pivot = array[0]
    pivots = [number for number in array if number == pivot]
    lesser = quick_sort([number for number in array if number < pivot])
    greater = quick_sort([number for number in array if number > pivot])

    return lesser + pivots + greater     
    
    
@timing
def sort_small_numbers_x_times(times, array, max_value):
    print "sorting small numbers {} times".format(times)
    for i in range(times):
        counting_sort(array, max_value)
        
@timing
def sort_big_numbers(times, array):
    print "sorting big numbers {} times".format(times)
    for i in range(times):
        quick_sort(array)  
        
if __name__ == "__main__":
  small_numbers = [randint(0,99) for i in range(11)]
  max_number = 99
  sort_small_numbers_x_times(100000, small_numbers, max_number)
  
  big_numbers = [randint(100,10000)**randint(100,10000) for i in range(10000)]
  sort_big_numbers(1, big_numbers)

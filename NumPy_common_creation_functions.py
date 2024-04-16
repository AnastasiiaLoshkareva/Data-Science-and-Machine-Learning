import numpy as np

# Task 1: Using np.array() - Write a Python function named create_array that takes a list of numbers as input and returns a numpy array containing those numbers.
def create_array(numbers):
    # Convert the list of numbers to a numpy array
    arr = np.array(numbers)
    return arr

# Test the function
numbers_list = [1, 2, 3, 4, 5]
result = create_array(numbers_list)
print(result)

# Task 2: Using np.zeros() - Write a Python function named create_zeros_array that takes two integers, rows and cols, as input and returns a 2D numpy array filled with zeros of size rows x cols.
def create_zeros_array(rows,cols):
    arr = np.zeros((rows,cols))
    return arr

rows = 5
columns = 5
result_arr = create_zeros_array(rows,columns)
print(result_arr)

# Task 3: Using np.ones() - Write a Python function named create_ones_array that takes two integers, rows and cols, as input and returns a 2D numpy array filled with ones of size rows x cols.
def create_ones_array(rows,cols):
    arr = np.ones((rows,cols))
    return arr

rows = 5
columns = 3
result_arr = create_ones_array(rows,columns)
print(result_arr)

# Task 4: Using np.arange() - Write a Python function named create_range_array that takes an integer stop as input and returns a 1D numpy array containing numbers from 0 to stop-1.
def create_range_array(stop):
    arr = np.arange(stop)
    return arr

stop = 10
result = create_range_array(stop)
print(result)

# Task 5: Using np.linspace() - Write a Python function named create_linspace_array that takes three parameters start, stop, and num and returns a 1D numpy array containing num evenly spaced numbers over the interval [start, stop].
def create_linspace_array(start,stop,num):
    arr = np.linspace(start,stop,num)
    return arr
start = 2
stop = 5
num = 7
result = create_linspace_array(start,stop,num)
print(result)


if __name__ == '__main__':
    main()

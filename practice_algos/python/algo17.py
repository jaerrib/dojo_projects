# 17. Double Vision - Given an array (similar to saying 'takes in an array'),
# create a function that returns a new array where each value in the original
# array has been doubled.  Calling double([1,2,3]) should return [2,4,6]
# without changing the original array

def double(arr):
    temp_arr = []
    for num in arr:
        temp_arr.append(num*2)
    return temp_arr

my_arr = [1,2,3]
print(f"Doubled array: {double(my_arr)}")
print(f"Original array: {my_arr}")
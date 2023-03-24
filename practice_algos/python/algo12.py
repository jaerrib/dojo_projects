# 12. Swap Values - Write a function that will swap the first and last values
# of any given array. The default minimum length of the array is 2. (e.g.
# [1,5,10,-2] will become [-2,5,10,1])

def swap_values(arr):
    temp_val = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp_val
    return arr


print(swap_values([1, 5, 10, -2]))

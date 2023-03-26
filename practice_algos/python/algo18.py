# 18. Count Positives - Given an array of numbers, create a function to
# replace the last value with the number of positive values found in the
# array.  Example, countPositives([-1,1,1,1]) changes the original array
# to [-1,1,1,3] and returns it

def countPositives(arr):
    num_pos = 0
    for num in arr:
        if num > 0:
            num_pos += 1
    arr[-1] = num_pos
    return arr

print(countPositives([-1,1,1,1]))
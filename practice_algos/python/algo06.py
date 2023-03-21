# 6. Find average - Given an array with multiple values, write a function
# that returns the average of the values in the array. (e.g. for
# [1,3,5,7,20] average is 7.2)

def find_average(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum / len(arr)

print(find_average([1, 3, 5, 7, 20]))
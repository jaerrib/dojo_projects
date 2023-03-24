# 11. Max/Min/Avg - Given an array with multiple values, write a function
# that returns a new array that only contains the maximum, minimum, and
# average values of the original array. (e.g. [1,5,10,-2] will return
# [10,-2,3.5])

def max_min_avg(arr):
    max = arr[0]
    min = arr[0]
    sum = 0
    for num in arr:
        if num >= max:
            max = num
        if num <= min:
            min = num
        sum += num
    avg = sum / len(arr)
    return [max, min, avg]


print(max_min_avg([1, 5, 10, -2]))

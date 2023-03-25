# 15. Print Low, Return High - Create a function that takes in an array of numbers.
# The function should print the lowest value in the array, and return the highest
# value in the array

def low_high(arr):
    low = arr[0]
    high = arr[0]
    for num in arr:
        if num < low:
            low = num
        if num > high:
            high = num
    print(low)
    return high

print(low_high([1,3,5,-7]))
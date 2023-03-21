# 5. Find max - Given an array with multiple values, write a function that
# returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)

# def find_max(arr):
#     This is the easy way using the built-in method
#     return max(arr)

def find_max(arr):
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max

print(find_max([-3,3,5,7]))

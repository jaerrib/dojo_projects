# 22. Add Seven - Build a function that accepts an array. Return a new array
# with all the values of the original, but add 7 to each. Do not alter the
# original array.  Example, addSeven([1,2,3]) should return [8,9,10] in a
# new array

def add_seven(arr):
    temp_arr = []
    for i in range(len(arr)):
        temp_arr.append(arr[i] + 7)
    return temp_arr

print(add_seven([1,2,3]))
# 23. Reverse Array - Given an array, write a function that reverses its
# values, in-place.  Example: reverse([3,1,6,4,2]) returns the same array,
# but now contains values reversed like so... [2,4,6,1,3].  Do this without
# creating an empty temporary array.  (Hint: you'll need to swap values)

def rev_array(arr):
    temp_val = 0
    for i in range(round(len(arr) / 2)):
        temp_val = arr[-(i + 1)]
        arr[(-(i + 1))] = arr[i]
        arr[i] = temp_val
    return arr


print(rev_array([3, 1, 6, 4, 2]))

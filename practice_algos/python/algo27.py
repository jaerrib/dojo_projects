# 27. Scale the Array - Given an array arr and a number num, multiply all
# values in the array arr by the number num, and return the changed array
# arr.  For example, scaleArray([1,2,3], 3) should return [3,6,9]

def scale_the_array(arr, num):
    for i in range(len(arr)):
        arr[i] = arr[i] * num
    return arr

print(scale_the_array([1, 2, 3], 3))
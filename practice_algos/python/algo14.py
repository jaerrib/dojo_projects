# 14. Biggie Size - Given an array, write a function that changes all
# positive numbers in the array to the string "big".  Example:
#  makeItBig([-1,3,5,-5]) returns that same array, changed to [-1,
# "big", "big", -5]

def make_it_big(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr


print(make_it_big([-1, 3, 5, -5]))

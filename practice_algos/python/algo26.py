# 26. Swap Toward the Center - Given an array, swap the first and last
# values, third and third-to-last values, etc.  Example:
# swapTowardCenter([true,42,"Ada",2,"pizza"]) turns the array into
# ["pizza", 42, "Ada", 2, true].  swapTowardCenter([1,2,3,4,5,6]) turns
# the array into [6,2,4,3,5,1].  No need to return the array this time

def swap_toward_center(arr):
    for i in range(round(len(arr) / 2)):
        if i % 2 == 0:
            temp_val = arr[-(i + 1)]
            arr[(-(i + 1))] = arr[i]
            arr[i] = temp_val
    return arr


print(swap_toward_center([True, 42, "Ada", 2, "pizza"]))
print(swap_toward_center([1, 2, 3, 4, 5, 6]))

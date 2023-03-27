# 24. Outlook: Negative - Given an array, create and return a new one
# containing all the values of the original array, but make them all
# negative (negative values should remain negative). Given [1,-3,5],
# return [-1,-3,-5]

def outlook_negative(arr):
    temp_arr = []
    for num in arr:
        temp_arr.append(-(abs(num)))
    return temp_arr


print(outlook_negative([1, -3, 5]))

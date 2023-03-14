# 9. Squares - Given an array with multiple values, write a function that
# replaces each value in the array with the value squared by itself.
# (e.g. [1,5,10,-2] will become [1,25,100,4])

def squares(arr):
    for i in range(len(arr)):
        arr[i] = arr[i]**2
    return arr

print(squares([1, 5, 10, -2]))
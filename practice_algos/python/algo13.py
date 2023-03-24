# 13. Number to String - Write a function that takes an array of numbers
# and replaces any negative values within the array with the string 'Dojo'.
# For example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2]

def num_to_str(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = "Dojo"
    return arr


print(num_to_str([-1, -3, 2]))

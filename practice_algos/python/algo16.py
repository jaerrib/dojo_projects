# 16. Print One, Return Another - Build a function that takes in an array of
# numbers. The function should print the second-to-last value in the array,
# and return the first odd value in the array

def print_return(arr):
    if len(arr) > 2:
        print(arr[-2])
    else:
        print("Length of array is less than 2")
    for num in arr:
        if num < 0:
            return num
    print("No odd numbers in array")
    return

# expected 4, -3
print(print_return([1,2,-3,4,5]))

# expected less than 2 and no odds message plus return None
print(print_return([1]))

# expected less than 2 and return -3
print(print_return([-3]))

# expected 4 and no odds message plus return none
print(print_return([1,2,3,4,5]))

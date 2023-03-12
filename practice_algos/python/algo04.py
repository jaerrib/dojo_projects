# 4. Iterate an array - Write a function that returns the sum of all the
# values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14)

def iterate_array(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

print(iterate_array([1, 2, 5]))
print(iterate_array([-5,2,5,12]))
# 7. Array odd - Write a function that would return an array of all the odd
# numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'append' method

def arr_odd():
    arr = []
    for i in range(1, 50):
        if i % 2 != 0:
            arr.append(i)
    return arr

print(arr_odd())

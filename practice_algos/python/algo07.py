# 7. Array odd - Write a function that would return an array of all the odd
# numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]).

def array_odd():
    temp_arr = []
    for i in range(1, 50):
        if i % 2 != 0:
            temp_arr.append(i)
    return temp_arr

print(array_odd())
# 25. Always Hungry - Create a function that accepts an array, and prints
# "yummy" each time one of the values is equal to "food".  If no array
# values are "food", then print "I'm hungry" once

def always_hungry(arr):
    count = 0
    for item in arr:
        if item == "food":
            print("yummy")
            count += 1
    if count == 0:
        print("I'm hungry")
    return


always_hungry(["food", 1, 2, "food", 3, "food"])
always_hungry([1, 2, 3])

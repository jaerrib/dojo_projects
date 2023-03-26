# 21. Previous Lengths - You are passed an array (similar to saying
# 'takes in an array' or 'given an array') containing strings.
# Working within that same array, replace each string with a number -
# the length of the string at the previous array index - and return
# the array.  For example, previousLengths(["hello", "dojo", "awesome"])
# should return ["hello", 5, 4]. Hint: Can for loops only go forward?

def previousLengths(arr):
    for i in range((len(arr) - 1), 0, -1):
        arr[i] = len(arr[i - 1])
    return arr

print(previousLengths(["hello", "dojo", "awesome"]))
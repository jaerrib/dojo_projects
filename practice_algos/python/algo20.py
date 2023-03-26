# 20. Increment the Seconds - Given an array of numbers arr, add 1 to
# every other element, specifically those whose index is odd (arr[1],
# arr[3], arr[5], etc).  Afterward, print each array value and
# return arr

def increment_the_seconds(arr):
    for i in range(len(arr)):
        if i % 2 != 0:
            arr[i] += 1
        print(arr[i])
    return arr

increment_the_seconds([1, 1, 1, 1, 1, 1, 1, 1])
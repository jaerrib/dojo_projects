# Median of Sorted Lists
#   Given two lists that are sorted but not necessarily the same length. find the median value.
#   For example, if given ([1,5,9], [1,2,3,4,5,6]), return 4. If the number of values is even,
#   return the average of the middle values. If given ([1,5,9], [1,2,3,4,5]), return 3.5
#   Second: Expand your function to accept three lists instead of two.
#   Third: Rework your function to correctly handle an arbitrary number of lists.

import math

# Instructor provided solution


def median_list(first, second):
    for value in second:
        first.append(value)
    first.sort()
    if len(first) % 2 == 0:
        return (first[math.floor(len(first)/2)] + first[math.floor(len(first)/2) - 1]) / 2
    return first[math.floor(len(first)/2)]


print(median_list([1, 5, 9], [1, 2, 3, 4, 5]))
print(median_list([1, 5, 9], [1, 2, 3, 4, 5, 6]))


# Refactored function that accepts a tuple containing any nyumber of lists

def median_lists(lists):
    joint_list = []
    for list in lists:
        joint_list += list
    joint_list.sort()
    midpoint = math.floor(len(joint_list) / 2)
    if len(joint_list) % 2 == 0:
        return (joint_list[midpoint] + joint_list[midpoint - 1]) / 2
    return joint_list[midpoint]


print(median_lists(([1, 5, 9], [1, 2, 3, 4, 5])))
print(median_lists(([1, 5, 9], [1, 2, 3, 4, 5, 6])))

print(median_lists(([1, 5, 9],
                    [1, 2, 3, 4, 5],
                    [3, 2, 7, 3],
                    [9, 3, 2, 7, 9, 1])))

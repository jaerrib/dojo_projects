# 3. Sum odd 5000 - Write a function that returns the sum of all the odd
# numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999)

def sum_odd():
    sum = 0
    for i in range (1, 5001):
        if i % 2 != 0:
            sum += i
    return sum

print(sum_odd())
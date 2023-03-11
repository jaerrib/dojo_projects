# 2. Get even 1000 - Write a function that would get the sum of all the even
# numbers from 1 to 1000.  You may use a modulus operator for this exercise

def get_even():
    arr = []
    for i in range(1, 1001):
        if i % 2 == 0:
            arr.append(i)
    return arr


print(get_even())

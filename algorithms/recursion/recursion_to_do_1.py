# Recursive Sigma
# Write a recursive function that given a number returns the sum of integers
# from 1 to that number. Example: rSigma(5) = 15 (1+2+3+4+5); rSigma(2.5) =
# 3 (1+2); rSigma(-1) = 0.
from math import floor

def r_sigma(number):
    if floor(number) < 1:
        return 0
    return floor(number) + r_sigma(floor(number) - 1)

print(r_sigma(5))
print(r_sigma(2.5))
print(r_sigma(-1))

# Recursive Factorial
# Given num, return the product of ints from 1 up to num. If less than zero,
# treat as zero. If not an integer, truncate. Experts tell us 0! is 1.
# # Fact(3) = 6 (1*2*3). Also, rFact(6.5) = 720 (1*2*3*4*5*6).

def fact(number):
    if floor(number) < 0:
        return 0
    if floor(number) == 0:
        return 1
    return floor(number) * fact(floor(number) - 1)

print(fact(3))
print(fact(6.5))
print(fact(0))
print(fact(-3))
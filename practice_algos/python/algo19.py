# 19. Evens and Odds - Create a function that accepts an array.  Every
# time that array has three odd values in a row, print "That's odd!".
# Every time the array has three evens in a row, print "Even more so!"

def evens_and_odds(arr):
    odd_count = 0
    even_count = 0
    for num in arr:
        if num < 0:
            odd_count += 1
            even_count = 0
            if odd_count == 3:
                print("That's odd!")
                odd_count = 0
        if num > 0:
            even_count += 1
            odd_count = 0
            if even_count == 3:
                print("Even more so!")
                even_count = 0

evens_and_odds([-1,-1,-1, 1, -1, 1, 1, 1, -1, 1, -1])
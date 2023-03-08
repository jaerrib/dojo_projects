# 1. Get 1 to 255 - Write a function that returns an array
# with all the numbers from 1 to 255

def get_1_to_255():
    arr = []
    for i in range(1, 256):
        arr.append(i)
    return arr
    
print(get_1_to_255())

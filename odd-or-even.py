# Odd or Even

# In this activity you will be writing code to create a function that determines whether a number is odd or even.

# Instructions

# If `num` is evenly divisible by 2, return the string "even".
# If `num` is NOT evenly divisible by 2, return the string "odd".

def oddOrEven(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

print(oddOrEven(5))
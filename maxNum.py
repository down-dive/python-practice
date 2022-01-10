# Max Num
# In this activity you will be writing code to create a function that returns the largest number present in a given array.
# Instructions
#    - Return the largest number present in the given `arr` array.

#      - e.g. given the following array:
arr = [1, 17, 5, 6];

#      - The following number should be returned:

#      17;

def maxNum(list):
    number = 0
    for i in list:
        if i > number:
            number = i
        else:
            continue
        print(i)

maxNum(arr)
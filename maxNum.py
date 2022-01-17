# Max Num
# In this activity you will be writing code to create a function that returns the largest number present in a given array.
# Instructions
#    - Return the largest number present in the given `arr` array.

#      - e.g. given the following array:
arr = [1, 17, 23, 5, 6];

#      - The following number should be returned:

#      17;

def max_num(list):
    number = list[0]
#   current_num = 0
    for i in list:
        current_num = list[i]
        if current_num > number:
            number = current_num
        else:
            continue
        print(current_num)

max_num(arr)
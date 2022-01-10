# Log Nums

# In this activity you will be writing code to create a function that prints all whole numbers from 1 to a given number.

# Instructions


#    - Print all numbers from `1` up to the given `nums` argument inclusive.
#     - e.g. given the number `5` as the `num` argument, the following should be printed to the console, one log at a time:

#        ```bash
#        1
#        2
#        3
#        4
#        5
#       ```

def logNums(num):
    for number in range(num):
        print(number)

logNums(10)
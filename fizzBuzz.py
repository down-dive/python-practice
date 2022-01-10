# Fizz Buzz
#In this activity you will be writing code to create a function that solves the [Fizz Buzz](https://en.wikipedia.org/wiki/Fizz_buzz) problem.
## Instructions
#    - Iterate through each number in the given array.
#    - If a number is evenly divisible by 3, print "Fizz" to the console.
#    - If a number is evenly divisible by 5 print "Buzz" to the console.
#    - Else print the number.
#      - e.g. given the following array: #     ```js
arr = [13, 14, 15, 16, 17, 18, 19, 20];
#     - The following should be printed to the console:
#     13;
#      14;
#     ("Fizz Buzz");
#      ("Fizz");
#      17;
#     ("Fizz");
#     19;
#      ("Buzz");

def fizzBuzz(array):
    for i in array:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:\
            print("Fizz")
        else:
            print(i)

fizzBuzz(arr)
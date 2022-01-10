# Is Palindrome

# In this activity you will be writing code to create a function that takes in a string and determines whether or not it is a palindrome.

# > A palindrome is defined as any string spelled the same forwards as it is backwards.

# Instructions

#    - Return `true` if the given string is a palindrome.

#    - Return `false` if the given string is not a palindrome.

#     - e.g. given the following string:

string = "racecar";

#      - The following should be returned:

#      true;

def isPalindrome(word):
    if word == word[::-1]:
        return True
    else:
        return "It's not a palindrome"

print(isPalindrome(string))
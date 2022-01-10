# Vowel Count
#In this activity you will be writing code to create a function that counts the number of vowels in a given string.

## Instructions

#    - Return the number of vowels present in `str`.

def vowelCount(word):
    vowel = 0
    for letter in word:
        if letter.lower() in "aeoui":
            vowel += 1

    print("Number of vowels in the word is: " + str(vowel))

vowelCount("Hellojrdthgaern twbsyhngfbarenydh tunbtvgs ytb")
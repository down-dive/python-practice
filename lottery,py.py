#lottery
import random
while True:
    name = input("What is your name?:")
    lets_play = input("Hello, {}! Would you like to play lottery?(y/n)".format(name))
    if lets_play == "n":
        print("No problem! We can play another time.")
    else:
        numbers = input("Great! Enter 5 digits please(1-10)")

        while numbers != (1,5,7,4,8):
              print("I'm sorry! Next time you'll get lucky!")
              break
        else:
             print("Congratulations! {}, you are the winner!".format(name))
               
        
         

# guess the number game in Python 
import random
random_number = random.randint(1,100)
victory = False
turns =0
while victory==False:
    Your_guess = input("Enter a number between 1 and 100 : ")
    turns +=1
    if random_number==int(Your_guess):
        print("You won!")
        print("Number of turns you have used: ",turns)
        victory == True
        break
    else:
     if random_number>int(Your_guess):
        print("Your Guess was low, Please enter a higher number")
     else:
        print("your guess was high, please enter a lower number")

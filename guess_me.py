import random

print ("Welcome to my Game")
guesses = 1
x = random.randint (1, 10)

while (guesses < 9006):
    guesses = guesses + 1
    guess = input("I am thinking of a number, what is it? ")
    
    guess= int(guess)
    if x == guess: 
        print("You Win!")
        break
    else:
        print ("Bad Guess")

    
           

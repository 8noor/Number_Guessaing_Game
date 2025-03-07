# Project: Number Guessing Game
# Author: [Anum Rajput]
# Date: [2025-03-07]

# Import necessary libraries
import random
def guess_the_number():
    """Project 2 : Number Guessing Game."""
    number = random.randint(1, 20)
    guesses_left = 7
    #Welcome massage
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")
    

    #loop generate random number
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        try:
            #Get user guess
            guess = int(input("Take a guess of another number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        #guess the secret number
        if guess < number:
            print("Too low number!")
        elif guess > number:
            print("Too high number!")
        else:
            print(f"Congratulations! You guessed the number in {7 - guesses_left + 1} tries.")
            return
        guesses_left -= 1
        #jab sub guess khatam ho jata hai 
    print(f"\nSorry, you didn't guess the number. The number was {number}.")
 
        
        
guess_the_number()

    
    


   




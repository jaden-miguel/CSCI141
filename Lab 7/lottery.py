# Author: Jaden Miguel
# Date: 21 May 2019
# Description: Lab 7 Code, String methods, Lottery.py

import random

def generate_winner(begin):
    """
    Generate a winning lottery pick. If begin starts or ends with 1, 2, or 3, return that as the winning pick; 
    otherwise, return a string containing one word (monkey, dragon, or snake) and one digit (1, 2, or 3) in either order. 
    The random choices are made independently, so the chance of each possible pick is equal.
    """
    # Cheat code: if the user enters a string beginning or ending with a digit when prompted to press enter to continue, 
    # use whatever they entered as the winning pick.
    if len(begin) > 0 and (begin[0] in "123" or begin[-1] in "123"):
        return begin
    # Otherwise, choose the winning pick randomly:
    rand_digit = str(random.randrange(1, 4))
    list_nums = ["monkey", "dragon", "snake"]
    rand_word = random.choice(list_nums)
    order = random.randrange(1, 100)
    if order % 2 == 0:
        pick = rand_word + rand_digit
    else:
        pick = rand_digit + rand_word
    return pick

def get_valid_guess():
    """
    Prompt the user until they enter a pick that contains one of the words (dragon, monkey, snake), 
    and either begins or ends with one of the numbers (1, 2, or 3). When a valid guess is entered, return it.
    """
    guess_check = False
    while not guess_check:
        guess = input("Enter your pick: ")
        if ("monkey" in guess or "snake" in guess or "dragon" in guess) and \
           ("1" in guess or "2" in guess or "3" in guess):
            guess_check = True
        else:
            if not ("1" in guess or "2" in guess or "3" in guess):
                print("You guessed one of the valid words, but not one of the numbers.")
            elif not ("monkey" in guess or "snake" in guess or "dragon" in guess):
                print("You didn't guess a valid word. But you guessed a number!")
    return guess

def main():
    """
    Generate a lottery pick and check whether a user has guessed it correctly.
    """
    welcome_message = """Welcome, and thanks for playing Lotter.io!
Let's see if you've won. Today's word choices are monkey, dragon, and snake; the digit choices were 1, 2, and 3. 
The winning pick is a word and a digit in either order. Press enter to begin:"""
    print(welcome_message)
    begin_input = input()  # Enter to continue (or enter a cheat code!)
    winning_pick = generate_winner(begin_input)  # Generate a winning lottery pick
    guess = get_valid_guess()  # Get a valid guess from the user:
    
    # Check the guess against the winning pick and provide detailed feedback
    if guess == winning_pick:
        print("You guessed perfectly! You win a model train!")
    else:
        correct_word = any(word in guess for word in ["monkey", "dragon", "snake"])
        correct_number = any(number in guess for number in ["1", "2", "3"])
        if correct_word and correct_number:
            if guess[0].isdigit() == winning_pick[0].isdigit():
                print("You guessed the correct word and number, but in the wrong order!")
            else:
                print("You guessed neither the correct word nor the correct number.")
        elif correct_word:
            print("You guessed the correct word, but not the correct number.")
        elif correct_number:
            print("You guessed the correct number, but not the correct word.")
        else:
            print("You guessed neither the correct word nor the correct number.")

if __name__ == "__main__":
    main()

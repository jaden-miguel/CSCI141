# Name: Jaden Miguel
# Date: 4/24/19
# Purpose: A3 program, guessing game

import random

def main():
    print("Let's play a letter guessing game! You need to guess two letters chosen randomly from the word 'bellingham'. The two letters may be the same!")
    mystery_string = "bellingham"
    letter1 = random.choice(mystery_string)
    letter2 = random.choice(mystery_string)
    
    try:
        user_input = int(input("How many times do you want to guess? (enter a number between 2-4): "))
        if not 2 <= user_input <= 4:
            print("Not a correct value, you must choose between 2-4. Exiting.")
            return
    except ValueError:
        print("Please enter a valid number. Exiting.")
        return

    correct_guesses = set()
    for attempt in range(user_input):
        if len(correct_guesses) == 2:
            print("You win! The letters were:", letter1, "and", letter2)
            return
        user_guess = input("Guess a letter: ").lower()
        if user_guess == letter1:
            correct_guesses.add(letter1)
            print(f"You guessed one of the letters correctly: {letter1}")
        if user_guess == letter2:
            correct_guesses.add(letter2)
            print(f"You guessed one of the letters correctly: {letter2}")
        if user_guess not in {letter1, letter2} or len(correct_guesses) < 2:
            print("Nope, try again.")
        if attempt == user_input - 1:
            print("You are out of tries! The correct letters were:", letter1, "and", letter2)

if __name__ == "__main__":
    main()

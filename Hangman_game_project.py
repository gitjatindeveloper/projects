# small project of hangman game

import random
import string
import time

def get_hint(word, guess_letter):
    # function to provide one random letter as a hint
    letter_hidden = [letter for letter in word if letter not in guess_letter]
    hint_letter = random.choice(letter_hidden)
    return hint_letter

def choose_word():
    # function for random choose of word
    word_list = ["mango", "banana", "guava", "papaya", "grapes", "watermelon", "pomegranate", "orange", "sweet lemon", "pineapple", "coconut", "jackfruit", "lychee", "custard apple", "amla", "strawberry", "indian blackberry", "indian plum", "kiwi"]
    return random.choice(word_list)

def display_word(word, guess_letter):
    # function to check the word
    display_word = ""
    for letter in word:
        if letter in guess_letter:
            display_word += letter
        else:
            display_word += "_"
    return display_word

def validate_input(guess):
    # validate the player input
    if guess == "hint" or (len(guess) == 1 and guess.isalpha() and guess in string.ascii_lowercase):
        return True
    else:
        print("Invalid input, please enter a single letter or 'hint'")
        return False

def hangman_game():
    # function for the main game
    word = choose_word()
    guess_letter = []
    incorrect_guesses = 0
    attempts_max = 5
    hint_used = False  # Initialize the hint usage status to False
    start_timer = time.time() # record starting time of the game

    print("Welcome to Hangman!")
    while True:
        print("\n" + display_word(word, guess_letter))

        if "_" not in display_word(word, guess_letter):
            end_timer = time.time() # record ending time of the game 
            game_duration = end_timer - start_timer # calculate time game is being player
            game_score = round(1000 / game_duration) # calculate score based on time taken
            print("Congratulations! You've guessed the word:", word)
            print("Your score are:", game_score)
            break

        guess = input("Guess a letter or type 'hint' for a hint: ").lower()

        # get a hint
        if guess == "hint" and not hint_used:
            letter_hint = get_hint(word, guess_letter)
            print("Hint: One of the letters is", letter_hint)
            hint_used = True  # Set hint_used to True to prevent further hints
            continue

        if guess == "hint" and hint_used:
            print("Sorry, you've already used the hint. Try guessing a letter.")
            continue

        if not validate_input(guess):
            continue

        if guess in guess_letter:
            print("You've already guessed this letter.")
        else:
            guess_letter.append(guess)
            if guess not in word:
                incorrect_guesses += 1
                print("Incorrect guess. Attempts left:", attempts_max - incorrect_guesses)
                if incorrect_guesses == attempts_max:
                    print("Game Over. The word was:", word)
                    break

# Run the game
hangman_game()
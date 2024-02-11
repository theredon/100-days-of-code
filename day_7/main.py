import random
from hangman_art import *
from hangman_words import word_list

chosen_word = random.choice(word_list)

print(logo)
# added for testing
print(f"The solution is {chosen_word}")

display = []
end_of_game = False
word_length = len(chosen_word)
lives = 6
user_guesses = []

for _ in range(word_length):
    display.append("_")

print(stages[lives])
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    while guess in user_guesses:
        guess = input("You have already guessed that letter before, try another: ")
    
    user_guesses.append(guess)

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    print(stages[lives])

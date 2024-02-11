import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

chosen_word = random.choice(word_list).lower()
end_of_game = False
word_length = len(chosen_word)
lives = 6
user_guesses = []

# Creates the display.
display = []
for _ in range(word_length):
    display.append("_")

print(stages[lives])
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    while guess in user_guesses:
        guess = input(f"You have already guessed the letter {guess} before, try another: ")
    user_guesses.append(guess)

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word. You lose a life.")
        lives -= 1
    else:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = chosen_word[position]

    print(f"{' '.join(display)}")
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("Congratulations!! You win!!")
    if lives == 0:
        end_of_game = True
        print(f"You lose.  The word was {chosen_word}")

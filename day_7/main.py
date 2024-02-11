import 

from hangman_words import word_list
chosen_word = random.choice(word_list)

from hangman_art import logo, stages
print(logo)
# added for testing
print(f"The solution is {chosen_word}")

display = []
end_of_game = False
word_length = len(chosen_word)
lives = 6

for _ in range(word_length):
    display.append("_")

print(stages[lives])
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    print(stages[lives])

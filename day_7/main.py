import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# added for testing
print(f"The solution is {chosen_word}")

display = []
position = 0

for i in range(len(chosen_word)):
    display.append("_")

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        display[position] = letter
    position += 1
    
print(display)
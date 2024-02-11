import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# added for testing
print(f"The solution is {chosen_word}")

display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display.append("_")

guess = input("Guess a letter: ").lower()

for position in range(word_length):
    if chosen_word[position] == guess:
        display[position] = chosen_word[position]
    
print(display)
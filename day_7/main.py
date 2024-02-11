import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# added for testing
print(f"The solution is {chosen_word}")

display = []
end_of_game = False
word_length = len(chosen_word)

for _ in range(word_length):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]
    
    print(display)
    
    if "_" not in display:
        end_of_game = True

print("You win!")
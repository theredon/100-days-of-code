import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

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

    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = chosen_word[position]
    else:
        lives -= 1

    print(stages[lives])
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
    if lives == 0:
        end_of_game = True
        print("You Lose")

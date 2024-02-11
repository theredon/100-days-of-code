import random

word_list = ["ardvark", "baboon", "camel"]
r = random.randint(0, 2)
word = word_list[r]

user_guess = input("Guess a letter: ")

for char in word:
    if user_guess == char:
        print("Right")
    else:
        print("Wrong")

print(word)
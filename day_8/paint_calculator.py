import math

def paint_calc(height, width, cover):
    number_of_cans = int(math.ceil((height * width) / cover))
    print(f"You will need {number_of_cans} cans of paint to cover the wall.")


test_h = int(input("What is the heigth of the wall? "))
test_w = int(input("What is the width of the wall? "))
coverage = int(input("How many sq feet does each can cover? "))
cans = paint_calc(height=test_h, width=test_w, cover=coverage)


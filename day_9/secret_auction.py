from art import logo
from os import system, name

run_continue = "yes"
bids = {}

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def check_bids(bids):
    highest_bidder = ""
    highest_bid = 0
    for key in bids:
        if bids[key] > highest_bid:
            highest_bidder = key
            highest_bid = bids[key]
    print(f"The highest bidder was {highest_bidder} with a bid of {highest_bid}")

print(logo)
print("Welcome to the secret auction program.")

while run_continue == 'yes':
    customer_name = input("What is your name?: ")
    customer_bid = int(input("What is your bid?: $"))
    bids[customer_name] = customer_bid
    run_continue = input("Are there any other bidders?  Type 'yes' or 'no'\n")
    if run_continue == 'yes':
        clear()
    else:
        clear()
        check_bids(bids=bids)


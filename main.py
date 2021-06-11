from replit import clear
from art import logo

print(logo)
print("Welcome to secret auction program.")

Bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    Name = input("What is your name?: ")
    Bid_price = int(input("What is your bid? : $"))
    Bids[Name] = Bid_price
    should_continue = input("are there any other bidders? Type 'yes' or 'no'. \n").lower()

    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(Bids)
    elif should_continue == 'yes':
        clear()

"""Following program works in a scenario where people are bidding via a machine and where they can't compete for bids. Each bid is kept unknown from the previous and other bidders.
At the end, the bidder with the highest bid wins hence revealing their name and an appropriate messsage.
Please make sure 'art.py' is in the same folder / location where the main code file is stored in order to eliminate the need to give the relative path. 
"""

import os
from art import logo


def findHighestBidder(bids):
    highestBid = 0
    winnersName = ""
    for biddersName in bids:
        if bids[biddersName] > highestBid:
            highestBid = bids[biddersName]
            winnersName = biddersName

    print(f"The winner is {winnersName} with a bid of ${highestBid}.")


print(logo)
bids = {}

continueBidding = True

while continueBidding:
    biddersName = input("Enter your name here: ")
    biddersAmount = int(input("Enter your bid here: $"))
    bids[biddersName] = biddersAmount
    moreBidders = input("Are there any more bidders? (Yes / No): ").lower()
    os.system('clear')

    if moreBidders == "no":
        continueBidding = False

findHighestBidder(bids)

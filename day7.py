# Advent of Code
# Day 7
import re
import numpy as np
from collections import Counter

def check_poker_hand(hand):
    counts = Counter(hand)
    num_counts = sorted(counts.values(), reverse=True)

    # Two pair
    if 2 in num_counts and num_counts.count(2) == 2:
        print("two pair: ", hand)
        return 26
    # Full house
    elif 3 in num_counts and 2 in num_counts:
        print("full house: ", hand)
        return 52
    # 5 of a kind
    elif 5 in num_counts:
        print("5 of a kind: ", hand)
        return 78
    # 4 of a kind
    elif 4 in num_counts:
        print("4 of a kind: ", hand)
        return 65
    # 3 of a kind
    elif 3 in num_counts:
        print("3 of a kind: ", hand)
        return 39
    # 2 of a kind
    elif 2 in num_counts:
        print("one pair: ", hand)
        return 13
    # High card
    else:
        print("high card: ", hand)
        return 0

card_mapping = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': 9,
    'Q': 10,
    'K': 11,
    'A': 12,
}

#---------------------------------------------------------------------
# part 1
total = 0
hand_list = [[] for _ in range(91)]
bid_list = [[] for _ in range(91)]

with open('input_day7.txt', 'r') as f:
    for line in f.readlines():
        hand, bid = line.strip().split(' ')
        index = int(card_mapping[hand[0]]) + check_poker_hand(hand)
        # If there is already a hand at the index, need to order them
        if hand_list[index]:
            sub_index = 0
            # Look through all hands with the same value
            for old_hand in hand_list[index]:
                for i in range(len(hand)):
                    # Go card by card, if the new hand has a higher card, move it up an index
                    if card_mapping[old_hand[i]] > card_mapping[hand[i]]:
                        break
                    elif card_mapping[old_hand[i]] < card_mapping[hand[i]]:
                        sub_index+=1
                        break
            hand_list[index].insert(sub_index, hand)
            bid_list[index].insert(sub_index, int(bid))
        else:
            hand_list[index] = [hand]
            bid_list[index] = [int(bid)]
                        
    hand_list = [item for sublist in hand_list if sublist for item in sublist]
    bid_list = [item for sublist in bid_list if sublist for item in sublist]
print(sum(list(map(lambda x, y: x * y, bid_list, list(range(1, len(bid_list)+1))))))
        


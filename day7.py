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
        return 26
    # Full house
    elif 3 in num_counts and 2 in num_counts:
        return 52
    # 5 of a kind
    elif 5 in num_counts:
        return 78
    # 4 of a kind
    elif 4 in num_counts:
        return 65
    # 3 of a kind
    elif 3 in num_counts:
        return 39
    # 2 of a kind
    elif 2 in num_counts:
        return 13
    # High card
    else:
        return 0

def find_replacement(input_string):
    # Remove all occurrences of 'J' from the input string
    stripped_string = input_string.replace('J', '')

    if not stripped_string:  # If the stripped string is empty after removing 'J's
        return 'A'

    # Count occurrences of each character in the stripped string using mapped values
    char_count = Counter(card_mapping[char] for char in stripped_string if char in card_mapping)

    if len(char_count) == 0:  # If there are no valid characters left after removing 'J's
        return 'No numbers remaining'

    max_occurrence = max(char_count.values())

    # Check if there are multiple maximum occurrences
    max_values = [value for value, count in char_count.items() if count == max_occurrence]

    # Case 1: No repeated numbers
    if max_occurrence == 1:
        return max(stripped_string, key=lambda x: card_mapping[x])

    # Case 2: One repeated number
    if max_occurrence == 2:
        repeated_value = max(max_values)
        return next(key for key, value in card_mapping.items() if value == repeated_value)

    # Case 3: Two or more repeated numbers
    if 2 < max_occurrence < 5:
        # If there are multiple maximum occurrences, choose the highest value
        highest_repeated_value = max(max_values)
        return next(key for key, value in card_mapping.items() if value == highest_repeated_value)

# part 1
#card_mapping = {
#    '2': 0,
#    '3': 1,
#    '4': 2,
#    '5': 3,
#    '6': 4,
#    '7': 5,
#    '8': 6,
#    '9': 7,
#    'T': 8,
#    'J': 9,
#    'Q': 10,
#    'K': 11,
#    'A': 12,
#}

# part 2
card_mapping = {
    'J': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
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
        
#---------------------------------------------------------------------
# part 2
total = 0
hand_list = [[] for _ in range(91)]
bid_list = [[] for _ in range(91)]

with open('input_day7.txt', 'r') as f:
    for line in f.readlines():
        hand, bid = line.strip().split(' ')
        if 'J' in hand:
            replacement_value = find_replacement(hand)
            replacement_hand = hand.replace('J', replacement_value)
            index = int(card_mapping[hand[0]]) + check_poker_hand(replacement_hand)
        else:
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
        


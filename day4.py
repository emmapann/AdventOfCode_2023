# Advent of Code
# Day 4
import re
import numpy as np

#---------------------------------------------------
# part 1
total = 0
with open('input_day4.txt', 'r') as f:
    for line in f.readlines():
        # split the game ID from rest of the line
        game_id, rest = line.split(':')
        game_num = re.findall("\d+", game_id)[0]
        # split winning numbers from your numbers
        win_nums, my_nums = rest.split('|')
        win_nums = [int(num) for num in win_nums.split()]
        my_nums = [int(num) for num in my_nums.split()]
        
        set1 = set(win_nums)
        set2 = set(my_nums)

        # Find intersection
        intersection = set1 & set2
        if intersection:
            total += 2**(len(intersection)-1)
print(total)

#---------------------------------------------------
# part 2
total = 0
card_multiplier = []

with open('input_day4.txt', 'r') as f:
    for line in f.readlines():
        # split the game ID from rest of the line
        game_id, rest = line.split(':')
        game_num = int(re.findall("\d+", game_id)[0])
        # split winning numbers from your numbers
        win_nums, my_nums = rest.split('|')
        win_nums = [int(num) for num in win_nums.split()]
        my_nums = [int(num) for num in my_nums.split()]
        
        set1 = set(win_nums)
        set2 = set(my_nums)

        # Find intersection
        intersection = set1 & set2
        while len(card_multiplier) < game_num + len(intersection):
                card_multiplier.append(1)

        if intersection:
            total += 2**(len(intersection)-1)            
            card_multiplier[game_num:game_num+len(intersection)] = [x + card_multiplier[game_num-1] for x in card_multiplier[game_num:game_num+len(intersection)]]
            
print("card multiplier", card_multiplier)
print(sum(card_multiplier))
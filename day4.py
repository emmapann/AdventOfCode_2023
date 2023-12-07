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
        
        # Find intersection
        intersection = set(win_nums) & set(my_nums)
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

        # Find intersection
        times_won = len(set(win_nums) & set(my_nums))
        while len(card_multiplier) < game_num + times_won:
            card_multiplier.append(1)

        if times_won:      
            card_multiplier[game_num:game_num+times_won] = [x + card_multiplier[game_num-1] for x in card_multiplier[game_num:game_num+times_won]]

print("card multiplier", card_multiplier)
print(sum(card_multiplier))
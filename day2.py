# Advent of Code
# Day 2
import re
import numpy as np

# Notes from Andrew
# arr =  [3, 6, 7]
# game_id, rest = arr.split(':')
# _, id = game_id.strip().split(' ')
# for set_colors in rest.strip().split(';'):
#     pass


avail_cubes = [12, 13, 14]
game_total = 0

#---------------------------------------------------------------------
# part 1
with open('input_day2.txt', 'r') as f:
    for line in f.readlines():
        # split the game ID from rest of the line
        game_id, rest = line.split(':')
        game_num = re.findall("\d+", game_id)[0]
        _, id = game_id.strip().split(' ')
        count = 0
        # split game sests
        for set_colors in rest.strip().split(';'):
            rgb = [0, 0, 0]
            # split colors in set
            for single_color in set_colors.split(','):
                # find number of one color
                num = re.findall("\d+", single_color)[0]
                # find corresponding color string
                color = "".join(re.split("[^a-zA-Z]*", single_color))
                # add number of cubes 
                match color:
                    case "red":
                        rgb[0] = int(num)
                    case "green":
                        rgb[1] = int(num)
                    case "blue":
                        rgb[2] = int(num)
            if all(np.subtract(avail_cubes,rgb) >= 0): 
                count += 1
        if count == len(rest.strip().split(';')):
            game_total += int(game_num)
        
print(game_total)

#----------------------------------------------------------------------------
# part 2
game_total = 0
with open('input_day2.txt', 'r') as f:
    for line in f.readlines():
        # split the game ID from rest of the line
        game_id, rest = line.split(':')
        game_num = re.findall("\d+", game_id)[0]
        _, id = game_id.strip().split(' ')
        count = 0
        min_rgb = [0, 0, 0]
        # split game sests
        rgb = [[0] * 3 for _ in range(len(rest.strip().split(';')))]
        for set_colors in rest.strip().split(';'):
            power = 1
            # split colors in set
            for single_color in set_colors.split(','):
                # find number of one color
                num = re.findall("\d+", single_color)[0]
                # find corresponding color string
                color = "".join(re.split("[^a-zA-Z]*", single_color))
                # add number of cubes 
                match color:
                    case "red":
                        rgb[count][0] = int(num)
                    case "green":
                        rgb[count][1] = int(num)
                    case "blue":
                        rgb[count][2] = int(num)
            count+=1
        col_max_values = [max(col) for col in zip(*rgb)]
        for num in col_max_values:
            power *= num
        game_total += power        
print(game_total)
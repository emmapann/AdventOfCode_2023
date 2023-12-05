# Advent of Code
# Day 5
import re
import string


#---------------------------------------------------------------------
# part 1
ss_dest_range = []
ss_source_range = []
sf_dest_range = []
sf_source_range = []
fw_dest_range = []
fw_source_range = []
fw_dest_range = []
fw_source_range = []
wl_dest_range = []
wl_source_range = []
lt_dest_range = []
lt_source_range = []
th_dest_range = []
th_source_range = []
hl_dest_range = []
hl_source_range = []
smallest_loc = []

with open('input_day5_test.txt', 'r') as f:

    # get each section
    sections = f.read().split('\n\n')  # Split based on a fully empty line

    # In this loop, we will just build up all of the mappings
    for section in sections:
        category, nums = section.strip().split(':')
        number_list = nums.strip().split('\n')
        int_list = [list(map(int, item.split())) for item in number_list]

        match category:
            case 'seeds':
                # create list of seeds
                seeds = sum(int_list, [])
                
                # part 2
                updated_seeds = []
                # TODO: this is SLOW
                for i in range(0, len(seeds)-1, 2):
                    new_list = list(range(seeds[i], seeds[i]+seeds[i+1]))
                    updated_seeds += new_list

            case 'seed-to-soil map':
                for set in int_list:
                    ss_dest_range.append([set[0], set[0]+set[2]-1])
                    ss_source_range.append([set[1], set[1]+set[2]-1])

            case 'soil-to-fertilizer map':
                for set in int_list:
                    sf_dest_range.append([set[0], set[0]+set[2]-1])
                    sf_source_range.append([set[1], set[1]+set[2]-1])

            case 'fertilizer-to-water map':
                for set in int_list:
                    fw_dest_range.append([set[0], set[0]+set[2]-1])
                    fw_source_range.append([set[1], set[1]+set[2]-1])

            case 'water-to-light map':
                for set in int_list:
                    wl_dest_range.append([set[0], set[0]+set[2]-1])
                    wl_source_range.append([set[1], set[1]+set[2]-1])
            
            case 'light-to-temperature map':
                for set in int_list:
                    lt_dest_range.append([set[0], set[0]+set[2]-1])
                    lt_source_range.append([set[1], set[1]+set[2]-1])
            
            case 'temperature-to-humidity map':
                for set in int_list:
                    th_dest_range.append([set[0], set[0]+set[2]-1])
                    th_source_range.append([set[1], set[1]+set[2]-1])
            
            case 'humidity-to-location map':
                for set in int_list:
                    hl_dest_range.append([set[0], set[0]+set[2]-1])
                    hl_source_range.append([set[1], set[1]+set[2]-1])

    # Loop over seeds
    first = True
    #for element in seeds:
    for element in updated_seeds:
        next = element
        count = 0
        for rng in ss_source_range:
            if rng[0] < element < rng[-1]:
                index = element - rng[0]-1
                next = int(ss_dest_range[count][0]) + int(index) + 1
                break
            elif next == rng[0]: 
                next = int(ss_dest_range[count][0])
                break
            elif next == rng[-1]:
                next = int(ss_dest_range[count][-1])
                break
            count +=1
        count = 0
        for rng in sf_source_range:
            if rng[0] < next < rng[-1]:
                index = next - rng[0]-1
                next = int(sf_dest_range[count][0]) + int(index) + 1
                break
            elif next == rng[0]: 
                next = int(sf_dest_range[count][0])
                break
            elif next == rng[-1]:
                next = int(sf_dest_range[count][-1])
                break
            count+=1
        count = 0
        for rng in fw_source_range:
            if rng[0] < next < rng[-1]:
                index = next - rng[0]-1
                next = int(fw_dest_range[count][0]) + int(index) + 1
                break
            elif next == rng[0]: 
                next = int(fw_dest_range[count][0])
                break
            elif next == rng[-1]:
                next = int(fw_dest_range[count][-1])
                break
            count+=1
        count = 0
        for rng in wl_source_range:
            if rng[0] < next < rng[-1]:
                index = next - rng[0]-1
                next = int(wl_dest_range[count][0]) + int(index) + 1
                break
            elif next == rng[0]: 
                next = int(wl_dest_range[count][0])
                break
            elif next == rng[-1]:
                next = int(wl_dest_range[count][-1])
                break
            count+=1
        count = 0
        for rng in lt_source_range:
            if rng[0] < next < rng[-1]:
                index = next - rng[0]-1
                next = int(lt_dest_range[count][0]) + int(index) + 1
                break
            elif next == rng[0]: 
                next = int(lt_dest_range[count][0])
                break
            elif next == rng[-1]:
                next = int(lt_dest_range[count][-1])
                break
            count +=1
        count = 0
        for rng in th_source_range:
            if rng[0] < next < rng[-1]:
                index = next - rng[0]-1
                next = int(th_dest_range[count][0]) + int(index) + 1
                break
            elif next == rng[0]: 
                next = int(th_dest_range[count][0])
                break
            elif next == rng[-1]:
                next = int(th_dest_range[count][-1])
                break
            count +=1
        count = 0
        for rng in hl_source_range:
            if rng[0] < next < rng[-1]:
                index = next - rng[0]-1
                next = int(hl_dest_range[count][0]) + int(index) + 1
                break
            elif next == rng[0]: 
                next = int(hl_dest_range[count][0])
                break
            elif next == rng[-1]:
                next = int(hl_dest_range[count][-1])
                break
            count +=1

        if first:
            smallest_loc = next
            first = False
        else:
            if next < smallest_loc: smallest_loc = next
print(smallest_loc)
            
            

       
        
        
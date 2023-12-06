import re
import time
start_time = time.time()

num_wins = 1
with open('input_day6.txt', 'r') as f:
    lines = f.readlines()
    times = lines[0].split(':')[1].replace(" ", "")
    times = [int(num) for num in times.split()]
    dist_record = lines[1].split(':')[1].replace(" ", "")
    dist_record = [int(num) for num in dist_record.split()]

    for t, d in zip(times, dist_record):
        for hold in range(0, t):
            time_remain = t - hold
            # Find first instance where combo beats record time,
            # then you know the pattern is symmetric do simple calc
            # to solve for number of win combos
            if (time_remain * hold) > d:
                num_wins*=(time_remain - hold + 1)
                break
print(num_wins)
print("--- %s seconds ---" % (time.time() - start_time))




    
        
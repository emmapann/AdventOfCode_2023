import numpy as np

# # part 1
# total = 0
# with open('input_day9.txt', 'r') as f:
#     for line in f.readlines():
#         num_as_str = line.split()
#         nums = np.array([int(num) for num in num_as_str])
#         #print(nums)

#         last_nums = []
#         last_nums.append(nums[-1])
        
#         # Calculate differences between consecutive elements using numpy.diff()
#         differences = np.diff(nums)
#         print(differences)
#         while any([x != 0 for x in differences]):
#             last_nums.append(differences[-1])
#             differences = np.diff(differences)
#             print(differences)
#         print("last nums: ", last_nums)
#         total += np.sum(np.array(last_nums))
#     print("total:", total)

# part 2
# total = 0
# with open('input_day9.txt', 'r') as f:
#     for line in f.readlines():
#         num_as_str = reversed(line.split())
#         nums = np.array([int(num) for num in num_as_str])
#         #print(nums)

#         last_nums = []
#         last_nums.append(nums[-1])
        
#         # Calculate differences between consecutive elements using numpy.diff()
#         differences = np.diff(nums)
#         print(differences)
#         while any([x != 0 for x in differences]):
#             last_nums.append(differences[-1])
#             differences = np.diff(differences)
#             print(differences)
#         print("last nums: ", last_nums)
#         total += np.sum(np.array(last_nums))
#     print("total:", total)


# part 2
total = 0
with open('input_day9.txt', 'r') as f:
    for line in f.readlines():
        num_as_str = line.split()
        nums = [int(num) for num in num_as_str]

        first_nums = [nums[0]]
        # Calculate differences between consecutive elements using numpy.diff()
        differences = np.diff(nums)
        while any([x != 0 for x in differences]):
            first_nums.append(differences[0])
            differences = np.diff(differences)
        start = 0
        for i in reversed(first_nums):
            start = i - start
        total += start
    print(f"{total=}")







# this is andrews joke
# part 2
# total = 0
# with open('input_day9.txt', 'r') as f:
#     for line in f.readlines():
#         d = list(map(int, reversed(line.split())))
#         nums = [d[-1]]
#         while any(d := np.diff(d)):
#             nums.append(d[-1])
#         total += sum(nums)
#     print(f"{total=}")
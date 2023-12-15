
import re
#---------------------------------------------------
# part 1
# with open('input_day15.txt','r') as f:
#     contents = f.read().strip() 

# total_val = 0
# # Split the content by commas to create a list
# words = contents.split(',')
# for word in words:
#     current_val = 0
#     #Determine the ASCII code for the current character of the string.
#     #Increase the current value by the ASCII code you just determined.
#     #Set the current value to itself multiplied by 17.
#     #Set the current value to the remainder of dividing itself by 256.
#     for char in word:
#         ascii_value = ord(char) 
#         current_val += ascii_value
#         current_val *= 17
#         current_val = current_val % 256
#     total_val += current_val

# print(total_val)

#-------------------------------------
# part 2
# first part = label (which box)
# second part = operation
#   (-) remove lens if present
#   (=) add lens with focal length
# third part = focal length

class Lens:
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length

with open('input_day15.txt','r') as f:
    contents = f.read().strip() 

total_val = 0

# Initialize an empty dictionary
boxes = {}

# Split the content by commas to create a list
words = contents.split(',')
for word in words:
    result = re.split('=|-', word)
    label = result[0]
    focal_len = []
    # If there is an equal sign, there will be another number
    if result[1]: focal_len = result[1]

    new_lens = Lens(label, focal_len)
    hash_val = 0

    # Find the HASH value of the label
    for char in label:
        ascii_value = ord(char) 
        hash_val += ascii_value
        hash_val *= 17
        hash_val = hash_val % 256
    
    # If (=), need to add lens
    # If the desired box is not empty...
    found = False
    if "=" in word:
        if boxes and hash_val in boxes:
            for index, lens in enumerate(boxes[hash_val]):
                # If the desired box already has an entry with the same label replace the lens
                if lens.label == label:
                    boxes[hash_val][index] = new_lens
                    found = True
            # If there does not exist lens with same label, add it
            if not found:
                boxes[hash_val].append(new_lens)
        else:
            boxes[hash_val] = [new_lens]
    else:
        if boxes and hash_val in boxes:
            for index, lens in enumerate(boxes[hash_val]):
                    # If the desired box already has an entry with the same label replace the lens
                    if lens.label == label:
                        del boxes[hash_val][index]
s = 0
for key, lens_list in boxes.items():
    #print(f"Contents at Key {key}:")
    for index, lens in enumerate(lens_list):
        s += (key+1)*(index+1)*int(lens.focal_length)
        #print(f"Label: {lens.label}, Focal Length: {lens.focal_length}")
    #print()  # Empty line for separation between lists

print(f"{s=}")


        


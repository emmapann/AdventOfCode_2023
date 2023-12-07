from collections import Counter

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

def find_replacement(input_string):
    # Remove all occurrences of 'J' from the input string
    stripped_string = input_string.replace('J', '')

    if not stripped_string:  # If the stripped string is empty after removing 'J's
        return 'No numbers remaining'

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
    if max_occurrence >= 2:
        # If there are multiple maximum occurrences, choose the highest value
        highest_repeated_value = max(max_values)
        return next(key for key, value in card_mapping.items() if value == highest_repeated_value)

# Example strings
input_string_1 = "2233J"
input_string_2 = "A3JJ5"
input_string_3 = "KTJJT"

# Finding replacements for the given input strings
result_1 = find_replacement(input_string_1)
result_2 = find_replacement(input_string_2)
result_3 = find_replacement(input_string_3)

print("Result 1:", result_1)  # Output for input_string_1
print("Result 2:", result_2)  # Output for input_string_2
print("Result 3:", result_3)  # Output for input_string_3

#!/usr/bin/env python3
def remove_chars(input_string):
    # Initialize an empty string to store the result
    result_string = ""

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is not 'c' or 'C'
        if char.lower() not in ['c', 'C']:
            # Append the character to the result string
            result_string += char

    return result_string
original_string = "Best School"
new_string = remove_chars(original_string)
print(new_string)


'''Write a program to remove the vowels from the input string.'''
# # declaring variables
# sentence=input("Enter a sentence")
# out_put=""
# vowels="AEIOUaeiou"
# # A for loop to check if vowels are in the sentence
# for char in sentence:
#     if char not in vowels:
#         out_put += char
#
# print(f"The new new sentence/word minus vowels is: {out_put}")
#
def ant_vowels():
    # Get the input string from the user
    input_value= input("Enter a sentence/word: ")

    # Create an empty string to store the output
    out_put = ""

    # Create a string of vowels
    vowels = "AEIOUaeiou"

    # Iterate over each character in the input string
    for char in input_value:
        # If the character is not a vowel, add it to the output string
        if char not in vowels:
            out_put += char

    # Return the output string
    return out_put

# Call the ant_vowels function and store the result in a variable
result = ant_vowels()

# Print the result
print(f"The new sentence/word minus vowels is: {result}")








"""a program that take in a string as a input
and prints in the last two"""
while True:
    # Input a sentence from the user
    sentence=input("Enter a string of words").strip()

    # Split the sentence into words and store them in a list called "words"
    words=sentence.split()

    # Check if the length of the "words" list is greater than or equal to 2
    if len(words) >= 2:
        # If the length of "words" is at least 2, print the second to last word
        """Note , if you use [-2] the code prints out the second last word
        instead of the lst two words"""
        print(words[-2:])
        break
    else:
    # If the length of "words" is less than 2, print an error message
       print("The sentence must have at least two words.")
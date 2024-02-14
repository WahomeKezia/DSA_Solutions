def is_pangram(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    # Remove all spaces and punctuation marks
    sentence = ''.join(e for e in sentence if e.isalnum())
    # Create a set of all letters of the alphabet
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    # Check if the sentence contains all the letters of the alphabet
    return alphabet <= set(sentence)

# Example usage
sentence = "The quick brown fox jumps over the lazy dog"
print(is_pangram(sentence)) # Output: True
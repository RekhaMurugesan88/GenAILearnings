def shift_letters(word):
    shifted = ''
    for char in word:
        if char.isalpha():
            # Handle lowercase letters
            if char.islower():
                shifted += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            # Handle uppercase letters
            else:
                shifted += chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
        else:
            shifted += char  # Keep non-letters as they are
    return shifted

# Example usage:
input_word = input("Enter a word or sentence: ")
shifted_word = shift_letters(input_word)
print("Shifted text:", shifted_word)

def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in word if char in vowels)
    return count

# Example usage:
input_word = input("Enter a word: ")
vowel_count = count_vowels(input_word)
print(f"Number of vowels in '{input_word}': {vowel_count}")

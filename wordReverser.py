def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

# Example usage:
input_sentence = input("Enter a sentence: ")
output = reverse_words(input_sentence)
print("Reversed Words:", output)

import re

def analyze_paragraph(text):
    # Count characters (including spaces and punctuation)
    char_count = len(text)

    # Count words (split by whitespace)
    word_count = len(text.split())

    # Count sentences (basic split by ., !, or ?)
    sentence_count = len(re.findall(r'[.!?]', text))

    return word_count, sentence_count, char_count

# Example usage:
paragraph = input("Enter a paragraph:\n")

words, sentences, characters = analyze_paragraph(paragraph)

print(f"\nWord Count     : {words}")
print(f"Sentence Count : {sentences}")
print(f"Character Count: {characters}")

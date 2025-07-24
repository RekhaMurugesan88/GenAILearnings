def extract_initials(full_name):
    # Split the name into words
    words = full_name.strip().split()

    # Extract the first letter of each word and capitalize it
    initials = ''.join(word[0].upper() for word in words if word)

    return initials

# Example usage:
name_input = input("Enter full name: ")
initials = extract_initials(name_input)
print("Initials:", initials)

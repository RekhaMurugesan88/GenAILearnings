def display_name_formats(full_name):
    # Split and clean the input
    parts = full_name.strip().split()

    if len(parts) < 2:
        return "Please enter at least first and last name."

    first = parts[0]
    last = parts[-1]
    middle = ' '.join(parts[1:-1]) if len(parts) > 2 else ''

    print("\n--- Name Formats ---")
    print(f"1. First Last      : {first} {last}")
    print(f"2. Last, First     : {last}, {first}")
    print(f"3. Initials        : {''.join([p[0].upper() for p in parts])}")
    print(f"4. UPPERCASE       : {full_name.upper()}")
    print(f"5. lowercase       : {full_name.lower()}")
    print(f"6. With Middle Name: {first} {middle} {last}" if middle else f"6. No Middle Name: {first} {last}")

# Example usage:
name_input = input("Enter full name: ")
display_name_formats(name_input)

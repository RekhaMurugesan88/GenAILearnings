def format_phone_number(number):
    # Ensure it's a string
    number = str(number)

    # Check if it has exactly 10 digits
    if len(number) == 10 and number.isdigit():
        return f"({number[:3]}) {number[3:6]}-{number[6:]}"
    else:
        return "Invalid input. Please enter a 10-digit number."

# Example usage:
input_number = input("Enter a 10-digit phone number: ")
formatted = format_phone_number(input_number)
print("Formatted Number:", formatted)

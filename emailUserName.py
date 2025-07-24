def extract_username(email):
    if '@' in email:
        username = email.split('@')[0]
        return username
    else:
        return "Invalid email address."

# Example usage:
email_input = input("Enter an email address: ")
username = extract_username(email_input)
print("Username:", username)

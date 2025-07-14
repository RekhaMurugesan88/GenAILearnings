# Create an empty list to store names
names = []

# Input 5 names from the user
for i in range(1, 6):
    name = input(f"Enter name {i}: ")
    names.append(name)

# Print each name and its length
print("\nNames and their lengths:")
for name in names:
    print(f"{name} - {len(name)} characters")

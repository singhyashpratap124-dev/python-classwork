# List containing names, empty strings, and names with numbers
names = ["Anu", "", "Ravi", "Meena", "", "kumar", "Arun25", "Priya"]

print("valid names:")

for name in names:
    name = name.strip()
    # Skip empty strings
    if name == "":
        continue
    number_found = False
    # Check each character separately
    for character in name:
        if character.isdigit():
            number_found = True
            break
    # Stop processing names if a number is found
    if number_found:
        print("Invalid name found:", name) 
        print("Processing stopped.")   
        break

    print(name)
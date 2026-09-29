# Funtion to convert a numeric character into a number
def character_to_number(character):
    if character.isdigit() and len(character) == 1:
        number = ord(character) - ord("0")
        return number
    else:
        return None

# Read a character from the user
character = input("Enter a numeric character (o-9): ")

# Call the function
result = character_to_number(character)

# Display the result
if result is not None:
    print("Character value:",character)
    print("Converted number:", result)
    print("Data type:"(result))
else:
    print('Invalid input. Enter only one numeric character.')

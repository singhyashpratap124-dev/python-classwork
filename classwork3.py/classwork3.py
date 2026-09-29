# Function to search for an element
def search_element(numbers, key):
    found = False

    for index in range(len(numbers)):
        if numbers[index] == key:
            print("Element found at index:", index)
            foud = True
            break
        if found == False:
            print("Element not found.")

# Read list elements from the user
numbers = list(
    map(int, input("Enter list elements separated by spaces: ").split())
)           

# Read the elements to search 
key = int(input("Enter the element to search: "))

# Call the function 
search_element(numbers, key)

# Accept numbers continuously and stop when a negative number is entered

while True:
    num = float(input("Enter a number: "))

    if num < 0:
        print("Negative number entered. Program stopped.")
        break

    print("You entered:", num)

# Password program with only three attempts

correct-password == "cloud123"

for attempt in range(3) :
    password = input("Enter password: ")

    if password == correct_password:
        print("access granted.")
        break
    else:
        print("Incorrect password.")

else:
    print("Maximum attempts reached. Access denied.")

    
# Accept numbers continuously and stop when a negative number is entered

while True:
    num = float(input("Enter a number: "))

    if num < 0:
        print("Negative number entered. Program stopped.")
        break

    print("You entered:", num)

# Password program with only three attempts

corret-password == "cloud123"

for attempt in range(3) :
    password = input("Enter password: ")

    if password == correct_password:
        print("access granted.")
        break
    else:
        print("Incorrect password.")

else:
    print("Maximum attempts reached. Access denied.")
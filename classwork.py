# Function to check whether the student passed all subjects 
def has_passed_all_subjects(mark1, mark2, mark3):
    passed = mark1 >= 40 and mark2 >= 40 and mark3 >= 40
    return passed
# Read marks from the user
mark1 = float(input("Enter Subject 1 mark: "))
mark2 = float(input("Enter Subject 2 mark: "))
mark3 = float(input("Enter Subject 3 mark: "))
#Validate the marks
valid_marks = (
    0 <=mark1 <=100
    and 0 <= mark2 <= 100
    and 0 <= mark3 <= 100
)
if not valid_marks:
    print("Invalid ,arks! Enter marks between 0 to 100.")
else:
    # call the funtion:
    Result=has_passed_all_subjects(mark1,mark2,mark3)
    print("passed all subjects:", Result)
    if Result:
        print("Result: PASS")
    else:
        print("Result: FAIL")
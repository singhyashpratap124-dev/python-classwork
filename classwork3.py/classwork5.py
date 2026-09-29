# Read array elements
numbers = list(
    map(int, input("Enter array elements separated by spaces: ").split())
)

# Read the threshold
threshold = int(input("Enter the threshold value: "))

smaller = []
greater_equal = []

# Partition the array
for number in numbers:
    if number < threshold:
        smaller.append(number)
    else:
        greater_equal.append(number)

# Combine both groups
partitioned_array = smaller + greater_equal

print("Original array:", numbers)
print("Values smaller than", threshold, ":", smaller)
print("Values greater than or equal to", threshold, ":", greater_equal)
print("Partitioned array:", partitioned_array)

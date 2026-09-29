numbers=list(map(int,input("enter the element of array by living space :").split()))
k=int(input("ENTER THE K VALUE (K smallest element will we found)"))
if k<1 or k>len(numbers):
    print("Invalid value of k ")
else:
    sorted_numbers=sorted(numbers)
    kth_smallest=sorted_numbers[k-1]

print("Original array:",numbers)
print("Sorted array:",sorted_numbers)
print("kthsmallest element:",kth_smallest)

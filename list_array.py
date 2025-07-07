# Empty list
x = []

# List with initial values
y = [1, 2,6, 3, 4, 5]

# List with mixed types
z = [1, "hello", 3.14, True]

# List methods
y.append(5)
print(y)
y.sort()
print(y)


# find the Lowest value in array 
print("\nfinding the lowest Values from array")
my_arr = [7,12,13,2,4]
min_val = my_arr[0]  # Initialize with the first element
for i in my_arr:
    if i < min_val:
        print(i)
        min_val=i

print("The minimum value is ",min_val)
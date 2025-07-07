# bubble Sort ALgorithems
my_arr= [64,34,25,12,22,11,90,5]
print(my_arr)
n = len(my_arr)
for i in range(n-1):
    for j in range(n-i-1):
        if my_arr[j]> my_arr[j+1]:
            my_arr[j+1],my_arr[j] = my_arr[j], my_arr[j+1]
    print(my_arr)


print("The sorted Array ", my_arr)


# Make the bubble sort more efficient 
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_arr[j]> my_arr[j+1]:
            my_arr[j+1],my_arr[j] = my_arr[j], my_arr[j+1]
            swapped = True
    if not swapped:
        break

print("Sorted array", my_arr)


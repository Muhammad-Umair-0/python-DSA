my_array = [65,34,25,5,22,11,90,12]
n = len(my_array)
print(n)
for i in range(n-1):
    min_index = i
    for j in range(i+1,n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i,min_value)

print("The Sorted Array", my_array)


# selection sort using swap 
my_array = [65,34,25,5,22,11,90,12]
for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    my_array[i],my_array[min_index]  = my_array[min_index],my_array[i]

print("The sorted array is \n",my_array)
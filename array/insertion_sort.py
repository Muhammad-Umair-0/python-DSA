#  test 
for i in range(1,10):
    for j in range(i-1,-1,-1):
        print(j, end=" ")

arr  =[64,34,25,12,22,11,90,5]
n = len(arr)
for i in range(1,n):
    insert_index = i
    current_value = arr.pop(i)
    for j in range(i-1,-1,-1):
        if arr[j] > current_value:
            insert_index=j
    arr.insert(insert_index, current_value)

print("\n The sorted array is :")
print(arr)


#improved insertion sort

arr = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(arr)
for i in range(1,n):
    insert_index = i
    current_value = arr[i]
    for j in range(i-1,-1,-1):
        if arr[j] > current_value:
            arr[j+1] = arr[j]
            insert_index = j
        else:
            break
    arr[insert_index] = current_value
    
print(arr)

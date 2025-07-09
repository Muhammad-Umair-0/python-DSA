def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] ==targetVal:
            return i
    
    return -1

arr = [0,2,4,5,2,5,4,3]
targetVal =3
result = linearSearch(arr, targetVal)

if result != -1:
    print(f"the {targetVal} found at index : {result}")
else:
    print(f"The {targetVal} not found")

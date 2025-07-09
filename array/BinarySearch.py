
# Binary Search in python
# examples by programiz


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if x == array[mid]:
            return mid

        elif x > array[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 15

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")


# suing Recursive Function
def binarySearch(array, x, low, high):
    if high>=low:
        mid = low+ (high-low)//2
        # if found at mid return it 
        if x ==array[mid]:
            return mid
        
        # Search the right half
        elif x> array[mid]:
            return binarySearch(array,x,mid+1,high)
        else:
            return binarySearch(array,x, low,mid-1)
    
    return -1

arr = [2,4,6,8,9,10,11,33,44,55]
x =44
result = binarySearch(arr,x,0,len(arr)-1)
if result != -1:
    print(f"The Emement {x} is found at index {result}")
else:
    print("The result not found")


ush 
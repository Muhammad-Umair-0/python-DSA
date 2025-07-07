
def countingsort(arr):
    max_val = max(arr)
    count = [0]*(max_val+1)

    while len(arr)>0:
        num = arr.pop(0)
        count[num] +=1
    print(count)

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -=1
    return arr

arr = [1,2,3,5,7,6,5,6,2,3,2,1,3,4,5,7,3]

sortedArr = countingsort(arr)
print(sortedArr)
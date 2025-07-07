#fabonic Series using For loop
prev1 = 1
prev2 = 0

for fibo in range(18):
    newFibo = prev1+prev2
    print(newFibo, end=" ")
    prev2 = prev1
    prev1 = newFibo


#fabonic serie using recursion
print("\n Fabonic Recusrion") 
print(0)
print(1)
count =2 

def fibonacci(prev1,prev2):
    global count
    if count<=19:
        newFibo = prev1+prev2
        print(newFibo,end=" ")
        prev2 = prev1
        prev1 = newFibo
        count +=1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)

#formula to find the n(th) fabonic number
# F(n) = F(n-1)+F(n-2)
print("\n recursion using Formula")
def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

print(F(19))
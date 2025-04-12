def fac(n):
    
    if(n==1 or n==0):
        return 1
    
    return n*fac(n-1)
n = int(input("Enter your Number: "))
print("Factorial of",n,"is :",fac(n))
print("The complexity for recursive function is O(nlogn)")
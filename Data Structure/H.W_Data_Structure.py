def o1(n, m):
    total = n * m
    print("/n Iteration is 1")

def oN(n, m):
    total = 0
    for i in range(1, n + 1):
        total += m
    print("M Iteration: ",n)
    
m = int(input("Enter 'a' for a*b : "))
n = int(input("Enter a 'b' for a*b : "))

o1(n, m)
oN(n, m)
def myfunction(n):
    for i in range(0,n+1):
        print("First Loop")
    
    j=1
    while(j<=n+1):
        print("Second Loop",j)
        j=j*2
        
    for i in range(0,100):
        print("Third Loop")
        
print("Function above will take time: ")
print("O(N) = Ol Log(N) = 0(100)")
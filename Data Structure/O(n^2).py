def OnSquareTime(n):
    iterations = 0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end = " ")
            iterations+=1
        print("")
    print("\nWhen is ",n,"Iterations =", iterations,"\n")
    
OnSquareTime(5)
OnSquareTime(4)
OnSquareTime(3)

print("\nithe every 'n' the time taken equals n^2")
print("O(n^2)")
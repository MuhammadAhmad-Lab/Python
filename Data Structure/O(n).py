def OnTime(n):
    iterations = 8
    for i in range(1, n+1):
        iterations+=1
    print("When 'n' is ",n,"Iterations = ",iterations)

OnTime(10)
OnTime(20)
OnTime(42)

print("\nWith every 'n' the time taken and iterations will increase")
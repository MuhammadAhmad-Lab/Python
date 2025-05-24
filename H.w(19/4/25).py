def xyz(n):
    n = int(input("Enter a number: "))
    if n>0:
        print("Positive Number")
        xyz(n)
    elif n==0:
        print("Zero")
        xyz(n)
    else:
        print("Negative Number")
        
xyz(9)
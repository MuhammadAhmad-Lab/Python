def setorNot(number,n):
    if number&(1 << (n - 1)):
        print("\nSet")
    else:
        print("\nNot Set")

number = int(input("Enter the Number: "))
n = int(input("ENTER THE BIT NUMBER: "))
setorNot(number,n)
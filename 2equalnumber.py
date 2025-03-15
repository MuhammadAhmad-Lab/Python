def checkIfSame(number1, number2):
    if ((number1 ^ number2)!= 0):
        print("Number are not equal: ")
    else:
        print("Both are equal")
number1 = int(input("Enter first number to compare: "))
number2 = int(input("Enter 2nd number to compare: "))
checkIfSame(number1,number2)
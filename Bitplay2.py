def checkIfSame(number1, number2):
    if ((number1^number2) != 0):
        print("Number are not eaual")
    else:
        print("Number are equal")
        
number1 = int(input("Enter first number to compare: "))
number2 = int(input("Enter second number: "))

checkIfSame(number1,number2)
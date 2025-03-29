def divide(ourDividend, ourDiviser):
    sign = (-1 if((ourDividend < 0)^
              (ourDiviser < 0))else 1);

    ourDividend = abs(ourDividend);
    ourDiviser = abs(ourDiviser);

    quotientNumber = 0
    tempNumber = 0

    for i in range(31, -1, -1):
       if (tempNumber + (ourDiviser << i)<= ourDividend):
         tempNumber += ourDiviser << i
         quotientNumber |= 1 << i
         
    if sign == 1:
         quotientnNumber = quotientNumber
    return quotientNumber

a = int(input("Enter a for a/b: "))
b = int(input("Enter b for a/b: "))
print("Result of",a, "/",b,"is",divide(a,b))
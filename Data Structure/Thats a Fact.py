def print_factors(number):
    print("The factor of ",number,"are: ")
    for i in range(1, number +1):
        if number % i == 0:
            print(i)
    
number = int(input("Enter your number is to find the factors: "))
print_factors(number)
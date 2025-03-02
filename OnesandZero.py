def numberOfBits(n):
    ones = 0 
    zero = 0
    
    while(n):
        
        if(n&1 == 1):
            ones+=1
        else:
            zero+=1
            
        n >>=1
    print("/n/nOnes =",ones,"/nZeros",zero)
    
number = int(input("Enter your Number: "))
numberOfBits(number)
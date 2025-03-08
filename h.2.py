def FirstSetBit(number):
    position = 1
    mask = 1
    
    while (not(number & mask)):
        mask = mask << 1
        positon += 1
    
    return position

number = int(input("Enter a Number: "))
print("Position of the first set bit: ",FirstSetBit(number))
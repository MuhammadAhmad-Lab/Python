def hcf(numberSmallest,numberLargest):
 while(numberSmallest):
     numberStore = numberSmallest
     numberSmallest =  numberLargest % numberSmallest
     numberLargest = numberStore
 return numberLargest

numberLargest = int(input("Enter the Larget Integer: "))
numberSmallest = int(input("Enter the Smallest Integer: "))

lcm = int((numberSmallest / hcf(numberSmallest,numberLargest))* numberLargest)
print("LCM is: ",lcm)
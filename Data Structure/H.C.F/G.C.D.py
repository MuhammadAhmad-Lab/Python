numberLargest = int(input("Enter the Larget Integer: "))
numberSmallest = int(input("Enter the Smallest Integer: "))
while(numberSmallest):
     numberStore = numberSmallest
     numberSmallest =  numberLargest % numberSmallest
     numberLargest = numberStore
     
print("The H.C.F is :", numberLargest)
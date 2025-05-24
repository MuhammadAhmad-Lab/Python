def ways(stairs):
    
    #Check corner case
    if stairs < 0:
        return 0
    #If no stairs left, return one as it reaches the top
    if stairs == 0:
        return 1
    twoSteps = 0
    oneStep = 0
    
    #It can only jump 2 stairs
    if(stairs >= 2):
        twoSteps = ways(stairs-2)    
    #Jump 1 if one or more stairs are left
    oneStep = ways(stairs-1)
    
    #Return total value
    return twoSteps+oneStep

stairs = int(input("Enter the number of steps: "))
print("Number of ways to climb stairs: ",ways(stairs))
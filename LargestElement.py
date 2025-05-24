def MaxElementArray(a):
    length = len(a)
    
    if length == 1:
        return(a[0])
    
    return max(a[0],MaxElementArray(a[1: ]))

a = [1,2,234,254,745,5,6,655]
print("Largest element in array: ",MaxElementArray(a))
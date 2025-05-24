def headrec(n,num):
    if n>num:
        return
    
    headrec( n + 1, num)
    print(n)

def tailrec(n,num):
     
     if n>num:
         return
     
     print(n)
     
     tailrec(n +1, num)
     
n = int(input("Enter integer: "))

headrec(1,n)
tailrec(1,n)

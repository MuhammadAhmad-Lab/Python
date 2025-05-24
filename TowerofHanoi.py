# program to move n disks in Tower of Hanoi

def Hanoi(n ,a, b, c):
    if n == 1:
        print("Move 1 from rod",a,"to rod",b)
        return
    #Move disks n-1 from a to b
    Hanoi(n-1, a, c, b)
    print("Move disk", n,"from",a,"to rod",b)
    Hanoi(n-1,c,b,a)

n=4
Hanoi(n, 'A', 'C', 'B')
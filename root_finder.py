def root_finder(a,b,c):
    d = (b**2) - (4*a*c)
    
    if (d>0):

        r1 = ((-b) + (d**0.5)) / 2*a

        r2 = ((-b) - (d**0.5)) / 2*a

        return (r1,r2)
    
    elif (d == 0):

        r1 = -( b / (2*a))
        r2 = "there is only 1 root"
        return (r1,r2)

    else:

        print("There is no reel roots")


print("ax^2+bx+c")
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

root1,root2 = root_finder(a,b,c)
print(root1,root2)
        
        

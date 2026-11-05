'''n=int(input("enter a number"))
for i in range(1,n+1):
    print("*")'''


#solid square pattern
n=int(input("enter a number"))
# Row
for i in range(1,n+1):
    #no of items
    for j in range(1,n+1):
        print("*",end="")
    print()

#h w hollow square
'''****
   *  *
   *  *
   ****'''

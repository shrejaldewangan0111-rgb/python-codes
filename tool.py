#import random
'''import math
x=3
value_of_e=math.e
print(value_of_e)'''

'''x=3
value_of_pi=math.pi
print(value_of_pi)'''

'''sqr_no = math.srrt(4)
print(sqr_no)

sqr_no = math.factorial(4)
print(sqr_no)'''


'''a=random.randint(1,100)
print(a)


l1=[1,2,3,4,5,6,7]
shuffle = random.shuffle(l1)
print(l1)'''

# OS, Time khud se try krke aana 

# STRIP
'''s1= " hello world "
#s2=s1.strip()
#s2 = s1.lstrip()
s2= s1.rstrip()
#print(s2)
print(f"rstrip : {s2}")'''


#STRIP
'''s5="This is my laptop"
s6=s5.split()
print(s6)


s5="This is my laptop"
s6=s5.split(" ")
print(s6)

s5="This is my laptop  "
s6=s5.split()
print(s6)'''

'''s5="Apple,Mango,Banana"
s6=s5.split()
print(s6)

s5="Apple,Mango,Banana"
s6=s5.split(",")
print(s6)'''

'''s5="Apple,Mango,Banana"
s6=s5.split(",",1)# here 1 represent that python ek baar hi element ko split kr skte ho baki jo bacha hai usse single element consider krega
# agr yha pr 2 likha hota to 2 hi element split hoga uske agge ka sara element single unit consider hoga
print(s6)'''

#s="Recursion is very Useful"
#1.print 1st letter and last
#2.print letters from index 2 to 5,6 to 1
#3.Reverse the string but do not change the original.
#4.Capitalize all the "e" of the given string and print the new string.

'''s="Recursion is very Useful"
print(s[0],s[-1])
print(s[2:6],s[6:1:-1])
print(s[ : :-1])'''


'''s="Recursion is very Useful"
temp=""
for i in s:
    if i=="e":
        temp+=i.upper()
    else:
        temp+=i
print(temp)
'''
    

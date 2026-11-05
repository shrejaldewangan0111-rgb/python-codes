'''x=10
def sum(x,y):
    x=9
    print(x)
    print(x+y)

print(x)
sum(10,55)'''

'''x=10
def sum():
    global x 
    x=9
    y=33
    print(x)

print(x)
#print(y) ismai y print nhi hoga kyuki wo defined nhi hai or wo def fun ke andar hai 
sum()
print(x)'''

#LAMBDA FUNCTION
#WRITE LAMBDA FUNCTION FOR SQUARE AND CUBE


'''m2=lambda x,y :x*y
print(m2(10,11))'''


'''square = lambda x : x*x
Cube = lambda y: y*y*y
print(square(5))
print(Cube(3))'''


# RECURSION
#factorial
'''n=5
f=1
for i in range(1,n+1):
    f*=i
print(f)'''

'''n=int(input())
# recursion function - factorial
#n*(n-1)
def f(n):
    #base condition
    if n==0 or n==1:
        return 1
    return n*f(n-1)

print(f(n))'''

# agr ksi program mai ek baar return function aa gya hai uske baad baar baar return function likha hai to o ek hi baar run hoga 
# agr first wla return run kr rha hai to baki niche ka sara code khatam mtlb baki niche ka kuch bhi run nhi hoga or agr first wla 
# return run nhi kiya to second wla krega fhir uske niche ka koi sa bhi return function kaam nhi krega


# practical question
'''n=int(input())
def f(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return(f(n-1)+ f(n-2))
print(f(n))'''


#write a recursive function to calculate the sum of all numbers from 1 to n
'''n=int(input())
def f(n):
    if n==1:
        return 1
    return n+f(n-1)
print(f(n))'''


# write a recurcive function to calculate (a)^b without using ** or pow()
a=int(input())
b=int(input())
def f(a,b):
    if b<=0 :
        return 1
    return a*f(a,b-1) 

print(f(a,b))

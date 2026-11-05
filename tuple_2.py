# WRITE FUNCTION TO PERFORM VALIDATION ON A GIVEN PASSWORD.
# WRITE A FUNCTION TO PRINT EACH ELEMENT OF THE GIVEN TUPLE BESIDES THERE INDEX sample output 0:10 1:20
# write a recrive function for same

'''def f():
    for i in range(len(t)):
        print(i,":",t[i])

t=(10,20,30,40)    
f()'''
#SAME QUESTION WITH RECURSION
#WRITE A FUNCTION TO REMOVE AN ELEMENT FROM A TUPLE REMOVE AN ELEMENT

#SWAP THE FIRST AND THE LAST ELEMENTS OF THE GIVEN TUPLE(10,20,30,40,50) TO (50,20,30,40,10)
'''t=(10,20,30,40,50)
def swap(t):
    #EDGE CASE 
    if len(t)==1:
    return t
    result=(t[-1],)+(t[1:-1])+(t[0],)
    return result
print(swap(t))'''

#WRITE A FUNCTION TO REVERSE A GIVEN TUPLE 
'''t=(10,20,30,40,50)
def reverse(t):
    rev = t[::-1]
    return rev
print(reverse(t))'''


# WRITE A FUNCTION TO ROTATE A GIVEN TUPLE BY K POSITION
t = (10,20,30,40,50)
def rotate(t,k):
    k = k%len(t)
    result = t[-k:]+t[:-k]
    return result
print(rotate(t,2))

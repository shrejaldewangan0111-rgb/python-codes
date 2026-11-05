'''t1=(10,20,30,40)
print(t1[ :3])
l1=["rungta",0,"true",40]
print(l1[ :1])

print("tuple")
for i in t1:
    print(i)

for i in range(len(t1)):
    print(t1[i])
print("list")
for i in l1:
    print(i) '''

l1 = [30,20,40,60]
'''(l1.append(60))
print(l1)'''

'''l1.insert(1,90)
print(l1)'''

'''l1.remove(60)
print(l1)'''

'''l1.pop(2)
print(l1)'''

'''x = l1.count(20)
print(x)'''

#print(l1.index(20))


# 16 sep

'''li3=[i for i in range(1,1001)]
print(li3)'''

'''li3 = (i for i in range(1,1001))
print(li3)'''


# create a list that contain only odd numbers between 1- 100.
'''li4 = [i for i in range(1,101) if i%2 !=0]
print(li4)'''

#create a list that contains the cubes of the numbers forms another pre existing list and check if the  given numbers are even.

'''l = [77,88,64,10,54,3,2]
l1 = [i**3 for i in l if i%2==0]
print(l1)'''


'''l1=[5,6,7,8]
l2=[1,2,3,4]
print(l1+l2)
#print(l1*l2)# this will show typr error because list ko list se multiply nhi kr skte
print(l1*3)

l1=(5,6,7,8)
l2=(1,2,3,4)
print(l1+l2)
#print(l1*l2)'''


# TUPLE UNPACKING
'''str_det = ("ravi",21,79)
name, age, marks_per = str_det
print(name)
print(age)
print(marks_per)'''

'''st1_det = ("ravi",21,79)
st1_list = tuple(st1_det)
print(st1_list)
print(type(st1_list ))

st2_det = tuple(st1_list)
print(st2_det)
print(type(st2_det))'''

#WRITE A FUNCTION TO REVERSE A LIST
l=[10,20,30,40,50]
#p=l[::-1]
#print(p)

'''def reverse_list(l):
    return l[::-1]
print(reverse_list(l))'''


'''def  rev_lst(lst):
    rev=[]
    for i in lst:
        rev.insert(0,i)
    return rev
print(rev_lst(l))'''

#a> WRITE A FUNCTION TO TAKE INPUT IN A LIST
#b> DEFINE A FUNCTION TO PRINT THE LARGEST AND SECOND LARGEST NUMBER

'''l=[20,39,48,50,10]

largest = 0
second = 0

for i in range(l):
    num = int(input("Enter number: "))

    if num > largest:
        second = largest
        largest = num
    elif num > second:
        second = num
print("largest =", largest)
print("Second Largest =", second)'''


# WRITE A FUNCTION CHECK WHAT ELEMENTS GIVES THE TARGET SUM IN THE GIVEN LIST:
# SAMPLE TEST CASE:
#TARGET=9
#L = [1,2,3,4,5,8]

'''l=[1,2,3,4,5,8]
def target_sum(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if (l[i]+l[j]==9):
                print(l[i],l[j])
target_sum(l)'''

# WRITE A PYTHON FUNCTION TO MOVE ALL THE ZEROS OF THE LIST TO THE END, KEEPING THE ORDER OF NON-ZERO ELEMENT
# SAMPLE TEST CASE:
# MOVE_ZEROS([0,1,0,3,12])
# OUTPUT[1,3,12,0,0]
l=[0,1,0,3,12]
non_zero=[i for i in l if i!=0]
no_of_zeros = len(l)-len(non_zero)








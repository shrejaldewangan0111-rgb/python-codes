'''str1="shrejal is good girl"
print(str1)
#length of string
print(len(str1))
# lower case
print(str1.lower())
#upper case
print(str1.upper())
# to find the letter 
print(str1.find('g'))
# to count number of times the letter come in sentence
print(str1.count('g'))
# to replace the string
print(str1.replace("shrejal","shreju"))
#  it will give output in boolean 
print(str1.islower())
print(str1.isupper())'''

# to print the single word in single line and multiple word in multiple line
'''str1="This is Rungta University"
for i in str1:
    print(i)'''

'''str1="This is Rungta University"
for i in str1:
    if (i.isupper()==True):
        print(i.lower())
    else:
        print(i.upper())   '''

# 11 sep
# count the number of vowels in the string
str1= "select a language"
str_v = "aeiouAEIOU"
count_v=0
for i in str1:
    if(i in str_v):
        count_v+=1
print(count_v)

#DICTIONARY
# WRITE A FUNCTION TO CALCULATE THE CHARACTER FREQUENCY RETURN A DICTIONARY WHICH SHOW THE COUNT OF ALL CHARACTERS IN THE GIVEN STRING
#S.T. FREQ_CAL("BANANA")
#OUTPUT{'b':1,'a':3,'n':2}
'''word="banana"
def freq_cal(word):
    empt_dict = {}
    for i in word:
        if i in empt_dict:
            empt_dict[i] +=1
        else:
            empt_dict[i] = 1
    return empt_dict

print(freq_cal(word))'''

# WRITE A FUNCTION TO PRINT THE KEY WHICH HAS THE MAX VALUE
# {X:2,Y:4,Z:9}
a = {'X':1,'Y':10,'Z':9}
#khud se
'''def max_val(a):
    max_value = 0
    max_key = ""
    for i in a:
        if a[i] > max_value:
            max_value = a[i]
            max_key = i
    return max_key
print(max_val(a))'''

#sir wala
'''dict = {"a":-10,"b":-1,"c":-11}
def max_f(dict):
    max_val = -(1)*(2**32)
    for i in dict:
        if dict[i] > max_val:
            max_val=dict[i]
            max_key = i
    return max_key


print(max_f(dict))'''

#WRITE A FUNCTION TO MERGE_ODD (D1,D2). MERGE TWO DICTIONARIES WHEN A KEY APPEARS IN BOTH ADD THE VALUES.
# S.T. D1={'A':1,'B':2} D2={'B':3,'C':4} MERGE_ADD(D1,D2)
#OUTPUT-> {'A':1,'B':5,'C':4}

'''d1={'a':1,'b':2}
d2={'b':3,'c':4}
def f(d1,d2):
    for i in d1:
        for j in d2:
            if d1[i]==d2[j]:
                d1[i]=(d1[i]+d2[j])
            else:
                return d1
print(f(d1,d2))'''

#30 OCT
#WRITE COMMON ELEMENT(A,B,C)RETURN THE SORTED LIST OF ELEMENT PRESENT IN ALL THREE SETS
# S.T. A={1,2,3,4} B={2,3,5} C={3,2,9} 
# COMMON ELEMENTS(A,B,C) OUTPUT->[2,3]
'''a={1,2,3,4}
b={2,3,5}
c={3,2,9}
def common_elements(a,b,c):
    d=[]
    for i in a:
        if i in b and i in c:
            d.append(i)
    return sorted(d)
print(common_elements(a,b,c))'''

# WRITE A FUNCTION FOR UNIQUE WORDS . COUNT THE NUMBER OF DISTINCT WORDS IN A SENTENCE
# S="THE CAT AND THE HAT" S.T. UNIQUE_WORDS(S) OUTPUT 4
'''s="The cat and the hat"
print(set(s))
def unique_words(s):
    x=s.lower().split()
    y=set(x)
    print(y)
    print(len(y))

unique_words(s)'''

#WRITE A FUNCTION ONLY_IN_ONE(A,B) WHICH RETURNS LIST OF ELEMENTS THAT APPEAR IN EXACTLY ON OF THE TWO LITS:
# S.T. A=[1,2,3] B=[2,3,4] ONLY_IN_ONE(A,B) OUTPUT [1,4]
a=[1,2,3]
b=[2,3,4]
def f(a,b):
    y=set(a)
    d=set(b)
    x=a|b
    z=a&b
    c=x-z
    print(c)


f(a,b)
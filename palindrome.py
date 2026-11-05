s=input()
clean_s = s.strip()
#function
#old method
#rev = clean_s[::-1]
#if (rev == clean_s):
#    print("is a palindrome")
#else:
#    print("not a palindrome")


'''def check_str_palindrome(s):
    cleaned = "".join(i.lower() for i in clean_s if i.isalnum())
    return cleaned == cleaned[::-1]
print(check_str_palindrome(clean_s))'''

# (i)write a function to count the number of vowels consonants numbers and special characters in a given string.
#(ii) and return the count in a term of dictionary

# write a function to remove duplicate characters from a given string  "s= Hello"
s = input()
clean_s= s.strip()
def f(s):
    temp= ""
    for i in s:
        if i not in temp:
            temp+=i
    return temp

print(f(clean_s))

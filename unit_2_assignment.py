# 1 write a program to print all prime numbers between 1 and n 
'''n = int(input("Enter number: "))

for num in range(2, n + 1):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        print(num, end=" ")'''

# 2 write a program to find the sum of prime numbers between 1 and n.
'''n = int(input("Enter numbeer: "))
sum = 0

for num in range(2, n + 1):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        sum = sum + num

print(sum)'''

# 3 write a program to print all factors of a given number.
'''n = int(input("Enter number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")'''

# 4 write a program to check whether a given nnumbe is a perfect number.
'''n = int(input("Enter number: "))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")'''


# 5 write a program to find the second largest number among n input numbers without sorting.
'''n = int(input("Enter n: "))

largest = 0
second = 0

for i in range(n):
    num = int(input("Enter number: "))

    if num > largest:
        second = largest
        largest = num
    elif num > second:
        second = num

print("Second Largest =", second) '''

# 6 write a program to repeatedly calculate the sum of digits until a single digit number is obtained.
'''n = int(input("Enter number: "))

while n >= 10:
    sum = 0

    while n > 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10

    n = sum

print(n)'''

# 7 write a program to perform a circular shift of a number by one digit
'''n = int(input("Enter number: "))

last = n % 10
n = n // 10

result = last

while n > 0:
    digit = n % 10
    result = result * 10 + digit
    n = n // 10

print(result)'''


# 8 write a program to check whether a number is an armstrong number.
'''n = int(input("Enter number: "))
temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit ** 3
    n = n // 10

if sum == temp:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")'''

# 9 write a program to find the frequency of every digit present in a number.
'''n = int(input("Enter number: "))

for i in range(10):
    temp = n
    count = 0

    while temp > 0:
        digit = temp % 10

        if digit == i:
            count = count + 1

        temp = temp // 10

    if count > 0:
        print(i, ":", count, end=", ")'''


# 10 write a program to find the second largest digit of a number without sorting.
'''n = int(input("Enter number: "))

largest = -1
second = -1

while n > 0:
    digit = n % 10

    if digit > largest:
        second = largest
        largest = digit
    elif digit > second and digit != largest:
        second = digit

    n = n // 10

print("Second Largest =", second)'''


# 11 write a program to find the sum of digits at even positon and odd positions seperately.
'''n = int(input("Enter number: "))

even = 0
odd = 0
pos = 1

while n > 0:
    digit = n % 10

    if pos % 2 == 0:
        even = even + digit
    else:
        odd = odd + digit

    pos = pos + 1
    n = n // 10

print("Even positions =", even)
print("Odd positions =", odd)'''

# 12 write a program to check whether all digits of a number are even .
'''n = int(input("Enter number: "))
count = 0

while n > 0:
    digit = n % 10

    if digit % 2 != 0:
        count = count + 1

    n = n // 10

if count == 0:
    print("All digits are even")
else:
    print("Not all digits are even")'''

# 13 write a program to check whether all digits of a number are in increasing order.
'''n = int(input("Enter number: "))
last = 10
flag = 1

while n > 0:
    digit = n % 10

    if digit >= last:
        flag = 0

    last = digit
    n = n // 10

if flag == 1:
    print("Increasing Order")
else:
    print("Not Increasing Order")'''

# 14 write a program to find the difference between the larets and smallest digit of a number.
'''n = int(input("Enter number: "))

largest = 0
smallest = 9

while n > 0:
    digit = n % 10

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    n = n // 10

difference = largest - smallest

print("Difference =", difference)'''

# 15 write a program to find the largest and second largest digits in a single traversal of the number.
n = int(input("Enter number: "))

largest = -1
second = -1

while n > 0:
    digit = n % 10

    if digit > largest:
        second = largest
        largest = digit
    elif digit > second:
        second = digit

    n = n // 10

print("Largest =", largest)
print("Second Largest =", second)
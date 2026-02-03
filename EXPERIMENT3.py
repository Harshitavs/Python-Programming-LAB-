#EXPERIMENT 3
"""
#1Find a factorial of a given no.
n = int(input("Enter a number:"))
factorial = 1
for   i in range(1 , n+1):
    factorial *= i
print("Factorial is:",factorial)


#2 Find whether the given number is Armstrong number.

n = int(input("Enter a number:"))
temp = n
sum_of_powers = 0
digits = len(str(n))

while temp>0:
    digit = temp % 10
    sum_of_powers += digit ** digits
    temp //= 10
if sum_of_powers == n:
    print("Armstrong Number")
else:
    print("Not armstrong number:")
    
    
#3  Print Fibonacci series up to given term. 
              
m = int(input("Enter number of terms:"))
a,b = 0,1
for i in range(m):
    print(a,  end="  ")
    a, b = b, a + b
    

#4Write a program to find if given number is prime number or not.
num = int(input("Enter a number: "))
prime = True

if num < 2:
    prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:   # <-- check divisibility by i
            prime = False
            break

print("Prime" if prime else "Not Prime")


#5  Check whether given number is palindrome or not.

num = input("Enter a number:")
if num == num[ :  :  -1]:  #reverse slice
    print("Palindrome")
else:
    print("Not palindrome")

#6 Write a program to print sum of digits.
num = int(input("Enter a number:"))
sumDigits = 0
while num>0:
    sumDigits += num % 10
    num //= 10
print("Sum of digits:" , sumDigits)

#7 Count and print all numbers divisible by 5 or 7 between 1 to 100.
count  = 0
for i in range(1, 101):
    if ( i % 5 == 0 or i  % 7 == 0):
        print(i , end  =" " )
        count += 1
print("\nCount:", count)


#8 Convert all lower cases to upper case in a string.
string = input("Enter a string:")
print("Upper case: " , string.upper())
  

#9Print the table for a given number:  
          #   5 * 1 = 5 
        #  5 * 2 = 10……….. 
n = int(input("Enter a number:"))
for i in range (1, 11):
    print(f"{n} * {i} = {n * i}")
"""
#10  Write a program to print the following pattern

#123454321 
#1234 *4321 
#123  * * 321 
#12   * * *  21 
#1    * * * *   1

n = 5 
for i in range(1, n + 1):
    
    for j in range(1, n - i + 2):
        print(j, end="")
 
    for j in range(1, i):
        print("**", end="") 
    for j in range(n - i + 1, 0, -1):
        
        if i == 1 and j == n:
            continue
        print(j, end="")

    print()
"""
#11  Write a program to print the sum of the following series 
 #1+ ½ + 1/3 + ¼ +….+1/n

n = int(input("Enter the valure of n:"))
sumOFSeries = 0.0
for i in range(1, n+1):
    sumOFSeries += 1 / i
print("Sum of series : " ,sumOFSeries)
"""







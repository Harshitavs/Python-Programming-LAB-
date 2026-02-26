# EXPERIMENT 6
#1
"""
def max_min(numbers):
    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum, minimum

#2
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Max and Min:", max_min(nums))

#2
def sum_ofcubes(n):
    total = 0
    for i in range(1, n):
        total += i**3
    return total

n = int(input("Enter a number N: "))
print("Sum of cubes less than N:", sum_ofcubes(n))

#3
def print_nums(n):
    if n == 0:
        return
    print_nums(n-1)
    print(n)

n   = int(input("Enter N:"))
print("Numbers from 1 to N:")
print_nums(n)


#4
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
terms = int(input("Enter number of terms:"))
print("Fibonacci Series")
for i in range(terms):
      print(fibonacci(i),end =" ")

      
#5
import math
volume_cone = lambda r, h: (1/3) * math.pi * r**2 * h

r = float(input("Enter radius of cone: "))
h = float(input("Enter height of cone: "))
print("Volume of cone:", volume_cone(r, h))

#6
nums = list(map(int, input("Enter numbers separated by space: ").split()))
max_min = lambda lst: (max(lst), min(lst))
print("Max and Min:", max_min(nums))


# 7
def greet(name, msg="Hello"):   # default argument
    print(msg, name)

def add_numbers(*args):         # variable length argument
    return sum(args)

name = input("Enter your name: ")
msg_choice = input("Enter a custom message or press Enter for default: ")

if msg_choice.strip() == "":
    greet(name)   # uses default
else:
    greet(name, msg_choice)   # keyword argument

nums = list(map(int, input("Enter numbers to add separated by space: ").split()))
print("Sum:", add_numbers(*nums))

#8
check_same = lambda d: len(set(d.values())) == 1

n = int(input("Enter number of key-value pairs: "))
data = {}
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

print("All values same?", check_same(data))

# 9
list1 = input("Enter keys separated by space: ").split()
list2 = input("Enter values separated by space: ").split()

my_dict = dict(zip(list1, list2))
print("Generated Dictionary:", my_dict)
"""


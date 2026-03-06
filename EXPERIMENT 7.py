#EXPERIMENT 7
"""
# 1 Add few names, one name in each row, in “name.txt file”. 
#a. Count no of names 
#b. Count all names starting with vowel 
#c. Find longest name 
filename = "name.txt"
n = int(input("Enter number of names: "))
with open(filename, "w") as f:
    for i in range(n):
        name = input(f"Enter name {i+1}: ")
        f.write(name + "\n")
# counts names
with open(filename, "r") as f:
    names = f.readlines()
print("Total names:", len(names))
# starting with vowels
vowels = "AEIOUaeiou"
count_vowel = sum(1 for name in names if name[0] in vowels)
print("Names starting with vowel:", count_vowel)
#longest name 
longest = max(names, key=len).strip()
print("Longest name:", longest

#2  Store integers in a file. 
#a. Find the max number 
#b. Find average of all numbers 
#c. Count number of numbers greater than 100
filename = "numbers.txt"
n = int(input("Enter number of integers: "))
with open(filename, "w") as f:
    for i in range(n):
        num = int(input(f"Enter integer {i+1}: "))
        f.write(str(num) + "\n")
with open(filename, "r") as f:
    numbers = [int(x.strip()) for x in f.readlines()]
# max number 
print("Max number:", max(numbers))
# average of all
print("Average:", sum(numbers)/len(numbers))
#no of numbers greater then 100
count_gt100 = sum(1 for x in numbers if x > 100)
print("Numbers greater than 100:", count_gt100)


#3  Assume a file city.txt with details of 5 cities in given format (cityname population(in lakhs) 
#area(in sq KM) ):
filename = "city.txt"
n = int(input("Enter number of cities: "))
with open(filename, "w") as f:
    for i in range(n):
        city = input("Enter city name: ")
        population = float(input("Enter population (in lakhs): "))
        area = float(input("Enter area (in sq km): "))
        f.write(f"{city} {population} {area}\n")


with open(filename, "r") as f:
    cities = [line.strip().split() for line in f.readlines()]


print("\nCity Details:")
for city in cities:
    print("Name:", city[0], "Population:", city[1], "Area:", city[2])


print("\nCities with population > 10 lakhs:")
for city in cities:
    if float(city[1]) > 10:
        print(city[0])
total_area = sum(float(city[2]) for city in cities)
print("\nSum of areas of all cities:", total_area)



"""
4   Input two values from user where the first line contains N, the number of test cases. The 
next N lines contain the space separated values of a and b. Perform integer division and print 
a/b. Handle exception in case of ZeroDivisionError or ValueError.
"""
N = int(input("Enter number of test cases: "))

for _ in range(N):
    try:
        a, b = input("Enter two values (a b): ").split()
        a, b = int(a), int(b)
        print(a // b)  
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
"""
#5 Create multiple suitable exceptions for a file handling program. 
filename = input("Enter filename: ")
try:
    with open(filename, "r") as f:
        data = f.read()
    print("File contents:\n", data)

except FileNotFoundError:
    print("Error: File not found!")
except PermissionError:
    print("Error: You don’t have permission to access this file!")
except Exception as e:
    print("Unexpected error:", e)

#6 Write a program to create a counter to show that how many times the program is executed
filename = "counter.txt"

try:
    with open(filename, "r") as f:
        count = int(f.read())
except FileNotFoundError:
    count = 0  
count += 1
with open(filename, "w") as f:
    f.write(str(count))

print("This program has been executed", count, "times.")
"""

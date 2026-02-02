#EXP 2

#1 WAP WHETHER A GIVEN NO IS DIVISBLE BY 3 AND 5 BOTH
Num = int(input("Enter the no you want to check:"))
if ( Num % 3 == 0 and Num %  5 == 0):
    print("The number is divisble by 3 and 5 both")
else :
    print("The number is not divisble by 3 and 5 both")


#2WAP WHETHER GIVEN NO IS MULTIPLE OF 5 OR NOT
num = int(input("Enter the no. you want to check:"))
if (num % 5 == 0):
              print("The num is multiple of 5")
else :
             print("The no is not a multiple of 5")
             
#3WAP find greatest among two no.s if no.s are equal print "no.s are equal
A = int(input("Enter the num: "))
B = int(input("Enter the num:"))
if ( A > B) :
    print(A, " is greater ")
elif (B>A):
    print(B, "is greater ")
else :
   print("Both numbers are equal")
    
#4WAP Find the greatest among three numbers assuming no two values are same.

a  = int(input("Enter first number"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if(a>b and a>c ):
    print(a,"is greater than", b, c)
elif(b>c and b>a):
    print(b,"is greater than",a,c)
else:
    print(c,"greater then",b,a)

#5WAP Check whether the quadratic equation has real roots or imaginary roots. Display the roots. 

import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

D = b**2 - 4*a*c

if D > 0:
    root1 = (-b + (D)**0.5) / (2*a)
    root2 = (-b - (D)**0.5) / (2*a)
    print("Roots are real and distinct.")
    print(f"Root1 = {root1}, Root2 = {root2}")
elif D == 0:
    root = -b / (2*a)
    print("Roots are real and equal.")
    print(f"Root = {root}")
else:
    realPart = -b / (2*a)
    imagPart = (-D)**0.5 / (2*a)
    print("Roots are imaginary (complex).")
    print(f"Root1 = {realPart} + {imagPart}i")
    print(f"Root2 = {realPart} - {imagPart}i")
    
#6Find whether a given year is a leap year or not.
Y =int(input("Enter the year:"))
if  (Y % 4 == 0 and Y% 100 != 0) or (Y % 400 == 0):
       print(Y,"is leap year")
else : 
    print("Not a leap year")
       

#7Write a program which takes any date as input and display next date of the calendar 
#e.g. 
#I/P: day=20 month=9 year=2005  
#O/P: day=21 month=9 year 2005

def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def next_date(day, month, year):
    month_days = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

    day += 1
    if day > month_days[month - 1]:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1

    return day, month, year

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

next_day, next_month, next_year = next_date(day, month, year)
print(f"Next Date: day={next_day} month={next_month} year={next_year}")


"""
#8Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects 
and calculate the percentage. 
CGPA=percentage/10 
CGPA range: 
0 to 3.4 -> F 
3.5 to 5.0->C+ 
5.1 to 6->B 
6.1 to 7-> B+ 
7.1 to 8-> A 
8.1 to 9->A+ 
9.1 to 10-> O (Outstanding)
"""
def calculate_grade(cgpa):
    if 0 <= cgpa <= 3.4:
        return "F"
    elif 3.5 <= cgpa <= 5.0:
        return "C+"
    elif 5.1 <= cgpa <= 6.0:
        return "B"
    elif 6.1 <= cgpa <= 7.0:
        return "B+"
    elif 7.1 <= cgpa <= 8.0:
        return "A"
    elif 8.1 <= cgpa <= 9.0:
        return "A+"
    elif 9.1 <= cgpa <= 10.0:
        return "O (Outstanding)"
    else:
        return "Invalid CGPA"

marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks of subject {i}: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5   
cgpa = percentage / 10
grade = calculate_grade(cgpa)

print("\n--- Grade Sheet ---")
print(f"Marks: {marks}")
print(f"Total: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"CGPA: {cgpa:.2f}")
print(f"Grade: {grade}")






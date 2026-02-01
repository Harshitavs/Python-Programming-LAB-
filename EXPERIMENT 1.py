#1Installation and set up of python

#2 Create a variable and Store your age and print its type
"""
age = 19
print(age,type(age))

#3 Declare a string variable called x and assign it the value hello . Pirnt out the value of x.
x = "HELLO"
print(x)
print(type(x))

#4 Take diffrent data types and print its value using print function.
Name = "Harshita" 
age = 19
Height = 169.8 
Is_student = True
lst = ["Maths" , "python" , "DSA"]
print(Name , type(Name))
print(age,type(age))
print(Height,type(Height))
print(Is_student , type(Is_student))
print(lst,type(lst))

#5 Declare three integers variable x,y,z  where  x = 9 , y = 7 , perform addition , substraction , multiplication , division , floor division
x = 9
y = 7
z = 0
print("sum" ,x + y)
print("substraction" ,x-y)
print("multiplication", x*y)
print("divison",x/y)
print("Floordiv",x//y)

#6 WAP  to compute the length of hypotenuse of a right triangle using pythagoras theorem .
A = float(input("Enter first side of the triangle:"))
B = float(input("Enter second side of the traingle:"))
Hypotenuse= (A**2 + B**2)**0.5

print("the Hypotenuse is : " , Hypotenuse)

#7 WAP TO Find simple intrest, and total amount.(P + SI)
P = 1000
R = 2
T =1
SimpleInterest = (P*R*T )/100
print("S.I = " ,SimpleInterest )
TotalAmount = P + SimpleInterest
print("Total Amt " , TotalAmount)

#8WAP find area of triangle when length if sides are given.
A = 3
B = 4
C = 5

S = (A + B + C)/2
AREA = (S*(S - A)* (S - B)* (S - C))**0.5
print(f"The area is " , AREA)

#9WAP to convert given seconds into hours , mins , and remaining secs.
Seconds = 3665
Hours = Seconds // 3600
remaining_Seconds = Seconds % 60
minutes = remaining_Seconds % 60
print(f"The conversion is  [H][M][s]" , Hours, minutes , remaining_Seconds)

#10 WAP to swap 2 no.s without   having extra variable
A =int(input("Enter first no. A:"))
B = int(input("Enter second no. B:"))
A =A+B
B= A-B
A = A-B
              
print("A  =",A )
print(" B=",B)

#11 WAP sum of first n natural no.s
            
N = int(input("Enter a number: "))

sum_N = N* (N + 1) // 2

print("Sum of first", N, "natural numbers is:", sum_N)

#12 WAP to build truth table for bitwise operator ,AND ,OR , XOR

print("A B | A&B A|B A^B")
print("-------------------")
for a in [0, 1]:
      for b in [0, 1]:
            print(f"{a} {b}  |  {a & b}   {a | b}   {a ^ b}")
            

  # 13 WAP to find left shift or right shift of the given no.          

num = int(input("Enter a number: "))
shift = int(input("Enter how many positions to shift: "))
choice = input("Enter 'L' for left shift or 'R' for right shift: ")
if choice == 'L':
    result = num << shift   
    print(f"{num} << {shift} = {result}")
elif choice == 'R':
    result = num >> shift   
    print(f"{num} >> {shift} = {result}")
else:
    print("Invalid choice! Please enter 'L' or 'R'.")

"""
#14  Using membership operator find whether a given number is in sequence (10,20,56,78,89)

S = (10,20,56,78,89)
A =  int(input("Enter no you want to find in sequence:"))
if A in S:
         print("The no. is in the sequnce " )
else :
             print("No. is not in sequence" )

         

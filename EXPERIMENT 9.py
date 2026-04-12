#1.Create a class of student (name, sap id, marks[phy,chem,maths] ). Create 3 objects by taking inputs from the user and display details of all students
"""
class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.phy = phy
        self.chem = chem
        self.maths = maths

    def display(self):
        print("\n--- Student Details ---")
        print(f"Name      : {self.name}")
        print(f"SAP ID    : {self.sap_id}")
        print(f"Physics   : {self.phy}")
        print(f"Chemistry : {self.chem}")
        print(f"Maths     : {self.maths}")
        
students = []
for i in range(3):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Enter name: ")
    sap_id = input("Enter SAP ID: ")
    phy = int(input("Enter Physics marks: "))
    chem = int(input("Enter Chemistry marks: "))
    maths = int(input("Enter Maths marks: "))

    student = Student(name, sap_id, phy, chem, maths)
    students.append(student)

print("\n========== All Students ==========")
for s in students:
    s.display()  

#2Add constructor in the above class to initialize student details of n students and implement following methods:

a)Display() student details
b)Find Marks_percentage() of each student
c)Display result() [Note: if marks in each subject >40% than Pass else Fail]
d)Write a Function to find average of the class.

class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.phy = phy
        self.chem = chem
        self.maths = maths

    def display(self):
        print("\n--- Student Details ---")
        print(f"Name      : {self.name}")
        print(f"SAP ID    : {self.sap_id}")
        print(f"Physics   : {self.phy}")
        print(f"Chemistry : {self.chem}")
        print(f"Maths     : {self.maths}")

    def find_marks_percentage(self):
        total = self.phy + self.chem + self.maths
        percentage = total / 3
        return percentage

    def display_result(self):
        if self.phy > 40 and self.chem > 40 and self.maths > 40:
            print(f"{self.name} Result: PASS")
        else:
            print(f"{self.name} Result: FAIL")

def class_average(students):
    total_percentage = 0
    for s in students:
        total_percentage += s.find_marks_percentage()
    avg = total_percentage / len(students)
    return avg

students = []
n = int(input("Enter number of students: "))
for i in range(n):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Enter name: ")
    sap_id = input("Enter SAP ID: ")
    phy = int(input("Enter Physics marks: "))
    chem = int(input("Enter Chemistry marks: "))
    maths = int(input("Enter Maths marks: "))

    student = Student(name, sap_id, phy, chem, maths)
    students.append(student)

print("\n========== Student Records ==========")
for s in students:
    s.display()
    print(f"Percentage: {s.find_marks_percentage():.2f}%")
    s.display_result()

print("\n========== Class Average ==========")
print(f"Average Percentage of Class: {class_average(students):.2f}%")


#3Create programs to implement different types of inheritances.

# 1. Single Inheritance
class Parent:
    def show_parent(self):
        print("Single Inheritance → Parent class")

class Child(Parent):
    def show_child(self):
        print("Single Inheritance → Child class")
        
# 2. Multiple Inheritance
class Father:
    def show_father(self):
        print("Multiple Inheritance → Father class")

class Mother:
    def show_mother(self):
        print("Multiple Inheritance → Mother class")

class ChildMultiple(Father, Mother):
    def show_child(self):
        print("Multiple Inheritance → Child class")


# 3. Multilevel Inheritance
class Grandparent:
    def show_grandparent(self):
        print("Multilevel Inheritance → Grandparent class")

class ParentMulti(Grandparent):
    def show_parent(self):
        print("Multilevel Inheritance → Parent class")

class ChildMulti(ParentMulti):
    def show_child(self):
        print("Multilevel Inheritance → Child class")


# 4. Hierarchical Inheritance
class ParentHier:
    def show_parent(self):
        print("Hierarchical Inheritance → Parent class")

class Child1(ParentHier):
    def show_child1(self):
        print("Hierarchical Inheritance → Child1 class")

class Child2(ParentHier):
    def show_child2(self):
        print("Hierarchical Inheritance → Child2 class")


# 5. Hybrid Inheritance (combination)
class A:
    def show_a(self):
        print("Hybrid Inheritance → Class A")

class B(A):
    def show_b(self):
        print("Hybrid Inheritance → Class B")

class C(A):
    def show_c(self):
        print("Hybrid Inheritance → Class C")

class D(B, C):  
    def show_d(self):
        print("Hybrid Inheritance → Class D")


# ------------------ DRIVER CODE ------------------
print("\n--- Single Inheritance ---")
s = Child()
s.show_parent()
s.show_child()

print("\n--- Multiple Inheritance ---")
m = ChildMultiple()
m.show_father()
m.show_mother()
m.show_child()

print("\n--- Multilevel Inheritance ---")
ml = ChildMulti()
ml.show_grandparent()
ml.show_parent()
ml.show_child()

print("\n--- Hierarchical Inheritance ---")
h1 = Child1()
h2 = Child2()
h1.show_parent()
h1.show_child1()
h2.show_parent()
h2.show_child2()

print("\n--- Hybrid Inheritance ---")
hy = D()
hy.show_a()
hy.show_b()
hy.show_c()
hy.show_d()

#4Create a class to implement method Overriding.

class Animal:
    def sound(self):
        print("Animals make different sounds.")

class Dog(Animal):
    def sound(self):
        print("Dog barks: Woof Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat meows: Meow Meow!")


print("--- Method Overriding Example ---")
a = Animal()
a.sound()   
d = Dog()
d.sound()   

c = Cat()


"""
#5Create a class for operator overloading which adds two Point Objects where Point has x & y values

#e.g. if
#P1(x=10,y=20)
#P2(x=12,y=15)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):   
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

print("--- Operator Overloading Example ---")
P1 = Point(10, 20)
P2 = Point(12, 15)

P3 = P1 + P2   

print("P1:", P1)
print("P2:", P2)
print("P3 = P1 + P2:", P3)



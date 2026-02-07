#Experiment 5
"""
#1. Scan n values in range 0-3 and print the number of times each value has occurred.
n = int(input("Enter no. of numbers :"))
count = [0,0,0,0]
for i in range(n):
    x = int(input(f"Enter number {i+1}(0-3):"))
    if 0<= x <=3:
        count[x] += 1
    else:
        print("The value should be 0-3 ")
print("\nResult  :")
print("0 appears",count[0],"times")
print("1 appears",count[1],"times")
print("2 appears",count[2],"times")
print("3 appears",count[3],"times")
                 

#2. Create a tuple to store n numeric values and find average of all values.
n = int(input("Enter how many values you want: "))

list = []

print("Enter", n, "numeric values:")
for i in range(n):
    num = float(input())   
    list.append(num)

tuple = tuple(list)

if n>0:
     average = sum(tuple) / len(tuple)

     print("Tuple is:", tuple)
     print("Average is:", average)

else:
    print("no values added")

#3 WAP to input a list of scores for N students in a list data type. Find the score of the runner
up and print the output. 
Sample Input 
N = 5 
Scores= 2 3 6 6 5 
Sample output 
5 
Note: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we 
print 5 as the runner-up score.

n =int(input("Enter no of students:"))
scores = []
print("Enter" ,n,"scores:")

for i in range(n) :
    s = int(input())
    scores.append(s)

largest  = scores[0]
for s in scores :
     if s > largest :
            largest = s
runner_up = None
for s in scores:
    if s != largest:

        if runner_up is None or s > runner_up:
            runner_up = s
print("Runner -up score is :" , runner_up)           
            


#4. Create a dictionary of n persons where key is name and value is city.  
#a) Display all names 
#b) Display all city names 
#c) Display student name and city of all students. 
#d) Count number of students in each city.

n = int(input("Enter number of persons: "))
students = {}

for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    students[name] = city

print("\nAll names:")
for name in students.keys():
    print(name)

print("\nAll cities:")
for city in students.values():
    print(city)

print("\nName and city of all students:")
for name, city in students.items():
    print(name, "->", city)

city_count = {}
for city in students.values():
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print("\nNumber of students in each city:")
for city, count in city_count.items():
    print(city, ":", count)


#5. Store details of n movies in a dictionary by taking input from the user. Each movie must 
store details like name,  year, director name, production cost, collection made (earning) & 
perform the following :- 
a) print all movie details 
b) display name of movies released before 2015 
c) print movies that made a profit.
d) print movies directed by a particular director.
#Create a dictionary of n persons where key is name and value is city.

n = int(input("Enter number of movies: "))
movies = {}
for i in range(n):
    name = input("\nEnter movie name: ")
    year = int(input("Enter release year: "))
    director = input("Enter director name: ")
    cost = float(input("Enter production cost: "))
    earning = float(input("Enter collection made: "))

    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "earning": earning
    }

print("\nAll movie details:")
for name, details in movies.items():
    print(name, ":", details)

print("\nMovies released before 2015:")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)

print("\nMovies that made a profit:")
for name, details in movies.items():
    if details["earning"] > details["cost"]:
        print(name)

search_director = input("\nEnter director name to search: ")
print("Movies directed by", search_director, ":")
for name, details in movies.items():
    if details["director"].lower() == search_director.lower():
        print(name)
        


#6. Create a contact book where users can store, search, update, and delete contacts. Use 
#dictionary for storing contacts.
#Create a contact book where users can store, search, update, and delete contacts. Use dictionary for storing contacts.

contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contacts[name] = number
    print("Contact added successfully!")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("Number of", name, "is", contacts[name])
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        number = input("Enter new number: ")
        contacts[name] = number
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def show_all_contacts():
    if contacts:
        print("\nAll Contacts:")
        for name, number in contacts.items():
            print(name, "->", number)
    else:
        print("No contacts available.")

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        show_all_contacts()
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


"""
#7. Create a Todo list Manager where users can add, view, and remove tasks. Use List for storing 
#taskS. 

#Create a Todo list Manager where users can add, view, and remove tasks. Use List for storing tasks.
todo = []
def add_task():
    task = input("Enter a new task: ")
    todo.append(task)
    print("Task added successfully!")

def view_tasks():
    if todo:
        print("\nYour Todo List:")
        for i, task in enumerate(todo, start=1):
            print(i, ".", task)
    else:
        print("No tasks in the list.")

def remove_task():
    view_tasks()
    if todo:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(todo):
            removed = todo.pop(num - 1)
            print("Removed task:", removed)
        else:
            print("Invalid task number.")

while True:
    print("\n--- Todo List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting Todo List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

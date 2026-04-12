#Exp 10
#1Create numpy array to find sum of all elements in an array.
"""
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

total = np.sum(arr)

print("Array elements:", arr)
print("Sum of all elements:", total)
"""
#2Create numpy array of (3,3) dimension. Now find sum of all rows & columns individually. Also find 2nd maximum element in the array.
"""
import numpy as np

arr = np.array([[10, 20, 30],
                [5, 25, 35],
                [12, 18, 40]])

print("Array:\n", arr)

row_sum = np.sum(arr, axis=1)
print("\nSum of each row:", row_sum)

col_sum = np.sum(arr, axis=0)
print("Sum of each column:", col_sum)


flattened = arr.flatten()          
sorted_arr = np.sort(flattened)   
second_max = sorted_arr[-2]       
print("\nSecond maximum element:", second_max)
"""
#3Perform Matrix multiplication of any 2 n*n matrices.
"""
import numpy as np

n = int(input("Enter the size of the matrix (n x n): "))

print("\nEnter elements of Matrix A:")
A = []
for i in range(n):
    row = list(map(int, input(f"Row {i+1} (enter {n} numbers): ").split()))
    if len(row) != n:
        raise ValueError(f"Row {i+1} must have {n} elements")
    A.append(row)
A = np.array(A)

print("\nEnter elements of Matrix B:")
B = []
for i in range(n):
    row = list(map(int, input(f"Row {i+1} (enter {n} numbers): ").split()))
    if len(row) != n:
        raise ValueError(f"Row {i+1} must have {n} elements")
    B.append(row)
B = np.array(B)

C = np.dot(A, B)

print("\nMatrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nResult of Matrix Multiplication (A x B):\n", C)
"""
#4Write a Pandas program to get the powers of an array values element-wise.
"""
Note: First array elements raised to powers from second array
Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
Expected Output:
X Y Z
0 78 84 86
1 85 94 97
2 96 89 96
3 80 83 72
4 86 86 83
"""
"""
import pandas as pd
data = {
    'X': [78, 85, 96, 80, 86],
    'Y': [84, 94, 89, 83, 86],
    'Z': [86, 97, 96, 72, 83]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

power_result = df['X'].astype(object) ** df['Y']

print("\nElement-wise power (X ** Y):")
print(power_result)
"""
#5Write a Pandas program to get the first 3 rows of a given DataFrame.
"""
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
First three rows of the data frame:
attempts name qualify score
a 1 Anastasia yes 12.5
b 3 Dima no 9.0
c 2 Katherine yes 16.5
"""
"""
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no',
                'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

print("First three rows of the data frame:")
print(df.head(3))
"""
#6Write a Pandas program to find and replace the missing values in a given DataFrame which do not have any valuable information.
"""
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James'],
    'score': [12.5, 9, np.nan, np.nan],
    'attempts': [1, 3, 2, 3],
    'qualify': ['yes', 'no', 'yes', 'no']
}

df = pd.DataFrame(exam_data)

print("Missing values in DataFrame:")
print(df.isnull())

df_filled = df.fillna(0)

print("\nDataFrame after replacing missing values:")
print(df_filled)
"""
#7Create a program to demonstrate different visual forms using Matplotlib.
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 2]
# ---- Line Plot ----
plt.figure()
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
# ---- Bar Chart ----
plt.figure()
plt.bar(categories, values)
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
# ---- Scatter Plot ----
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
# ---- Pie Chart ----
plt.figure()
plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

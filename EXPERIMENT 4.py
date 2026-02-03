#EXPERIMENT 4
"""
#1.  Write a program to count and display the number of capital letters in a given string.
s = input("Enter a string: ")
count = sum(1 for ch in s if ch.isupper())
print("Number of capital letters:", count)

#2.  Count total number of vowels in a given string.
s = input("Enter a string: ").lower()
vowels = "aeiou"
count = sum(1 for ch in s if ch in vowels)
print("Number of vowels:", count)

#3.  Input a sentence and print words in separate lines.
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word)
"""   
#4. WAP to enter a string and a substring. You have to print the number of times that the
#substring occurs in the given string. String traversal will take place from left to right, not 
#from right to left. 
#Sample Input 
#ABCDCDC
 #   CDC 
#Sample Output 
#2 
string = input("Enter main string: ")
substring = input("Enter substring: ")

count = 0
for i in range(len(string) - len(substring) + 1):
    if string[i:i+len(substring)] == substring:
        count += 1

print("Occurrences:", count)

"""
#5Given a string containing both upper and lower case alphabets. Write a Python program to 
#count the number of occurrences of each alphabet (case insensitive) and display the same. 
#Sample Input 
#ABaBCbGc 
#Sample Output 
#2A 
#3B 
#2C 
#1G

s = input("Enter a string: ").lower()
freq = {}

for ch in s:
    if ch.isalpha():
        freq[ch] = freq.get(ch, 0) + 1

for ch in sorted(freq):
    print(f"{freq[ch]}{ch.upper()}")
    

#6. Program to count number of unique words in a given sentence using sets.
sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)
print("Unique word count:", len(unique_words))   


#7. Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
#a) Fruits which are in both sets s1 and s2
#b) Fruits only in s1 but not in s2 
#c) Count of all fruits from s1 and s2
n = int(input("Enter number of fruits in each set: "))
s1 = set(input("Enter fruit for set 1: ") for _ in range(n))
s2 = set(input("Enter fruit for set 2: ") for _ in range(n))

print("Common fruits:", s1 & s2)
print("Fruits only in s1:", s1 - s2)
print("Total unique fruits:", len(s1 | s2))


#8. Take two sets and apply various set operations on them : 
#S1 = {Red ,yellow, orange , blue } 
#S2 = {violet, blue , purple}
S1 = {"Red", "yellow", "orange", "blue"}
S2 = {"violet", "blue", "purple"}

print("Union:", S1 | S2)
print("Intersection:", S1 & S2)
print("Difference (S1 - S2):", S1 - S2)
print("Symmetric Difference:", S1 ^ S2)

"""

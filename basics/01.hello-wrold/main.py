print("hello world!")

# variables
name = "Omelian"
age = 25
print("The dude name is " + name + ". He's " + str(age) + " years old.")

# numbers
from math import *
integer = 10
double = 3.0
print(integer / double)
print(sqrt(integer))

# IO operations
# name = input("Enter your name:")
# print(name)

# arrays and IO
words = ["kek", 1, "what"]
print(words[1:422]) # this still works for some reason
print(words[0:]) # print all


# list functions
list_one = [1,2,3]
list_two = ["a", "b", "c"]
# adding, extending a list
list_one.extend(list_two)
print(list_one)
# add single, append at item
list_one.append(23)
print(list_one)
# inserting insert(index, element)
list_two.insert(1, "a1")
print(list_two)
# delete, clear, pop - remove the last
list_two.pop()
print(list_two)
# search, index(key)
print(list_one.index("a"))
# count
print(list_one.count("a"))
# sort
# print(list_one.sort()) - wont work cos different types
# reverse
print(list_one.reverse())
# copy
list_three = list_one.copy()
print(list_three)
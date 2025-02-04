#A tutorial to familiarize with Python!!!
from operator import ifloordiv

#Getting started with variables.
#I can start by doing this: Let's use x and y for main variable name globally

#Array
fruits = ["apple", "orange", "mango", "banana", "strawberry"]
print(fruits) #Print whole array

print(fruits[0])#Print single index from an array

print(fruits[2:4])#Print from index x to index y

#Hello world
print("Hello, World!") #merge this to v0.2


#Traverse the array
# using for loop
for w in fruits:
    print(w, len(w))


#Create a collection
user_ID = {'Sab': '1234', 'Jonas': '4325', 'Linly': '143'}

#Iterate over a copy?
for user, id_num in user_ID.copy().items():
    if id_num == '1234':
        del user_ID[id_num]

remaining_user = {}
for user, id_num in user_ID.copy().items():
    if id_num == '143':
        remaining_user[user_ID] = id_num

'''
Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.
Set items are unchangeable, but you can remove items and add new items.
Sets are written with curly brackets.
'''

#Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: the set list is unordered, meaning: the items will appear in a random order.

#Once a set is created, you cannot change its items, but you can remove items and add new items.



#Sets cannot have two items with the same value.

#Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)



#The values True and 1 are considered the same value in sets, and are treated as duplicates:

#True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)



#The values False and 0 are considered the same value in sets, and are treated as duplicates:

#False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)




#To determine how many items a set has, use the len() function.

#Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}

print(len(thisset))




#Set items can be of any data type:

#String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}




<class 'set'>

#What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))





#It is also possible to use the set() constructor to make a set.

#Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
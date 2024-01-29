#append()	Adds an element at the end of the list

#Add an element to the fruits list:

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")

print(fruits)

#Add a list to a list:

a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

a.append(b)

print(a)

#clear()	Removes all the elements from the list

#Remove all elements from the fruits list:

fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits)

#copy()	Returns a copy of the list

#Copy the fruits list:

fruits = ["apple", "banana", "cherry"]

x = fruits.copy()

print(x)

#count()	Returns the number of elements with the specified value

#Return the number of times the value "cherry" appears in the fruits list:

fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)

#Return the number of times the value 9 appears int the list:

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)

#extend()	Add the elements of a list (or any iterable), to the end of the current list

#Add the elements of cars to the fruits list:

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)

#Add a tuple to the fruits list:

fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)

#index()	Returns the index of the first element with the specified value

#What is the position of the value "cherry":

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)

#What is the position of the value 32:

fruits = [4, 55, 64, 32, 16, 32]

x = fruits.index(32)  

print(x)   3 

#The index() method only returns the first occurrence of the value.


#insert()	Adds an element at the specified position

#Insert the value "orange" as the second element of the fruit list:

fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

#pop()	Removes the element at the specified position

#Remove the second element of the fruit list:

fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)

#Return the removed element:

fruits = ['apple', 'banana', 'cherry']

x = fruits.pop(1)

print(x)

#The pop() method returns removed value.


#remove()	Removes the item with the specified value
#Remove the "banana" element of the fruit list:

fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")

print(fruits)

#reverse()	Reverses the order of the list

Reverse the order of the fruit list:

fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)

#sort()	Sorts the list

#Sort the list alphabetically:

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)

#Sort the list descending:

cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)

print(cars)

#Sort the list by the length of the values:

# A function that returns the length of the value:

def myFunc(e):
    return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(cars)

#Sort a list of dictionaries based on the "year" value of the dictionaries:

# A function that returns the 'year' value:

def myFunc(e):
    return e['year']

cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

print(cars)

#Sort the list by the length of the values and reversed:

# A function that returns the length of the value:

def myFunc(e):
    return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

print(cars)

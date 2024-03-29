#A dictionary can contain dictionaries, this is called nested dictionaries.

#Create a dictionary that contain three dictionaries:

myfamily = {

  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },

  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },

  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)



#Or, if you want to add three dictionaries into a new dictionary:

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}




#To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

#Print the name of child 2:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])
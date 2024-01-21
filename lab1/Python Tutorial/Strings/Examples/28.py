#capitalize()	Converts the first character to upper case
#Upper case the first letter in this sentence:

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)    Hello, and welcome to my world.

#casefold()	Converts string into lower case
#Make the string lower case:

txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)    hello, and welcome to my world!

#center()	Returns a centered string
#Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:

txt = "banana"

x = txt.center(20, "O")

print(x)    OOOOOOObananaOOOOOOO

#count()	Returns the number of times a specified value occurs in a string
#Return the number of times the value "apple" appears in the string:

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)   2

#encode()	Returns an encoded version of the string
#UTF-8 encode the string:

txt = "My name is Ståle"

x = txt.encode()

print(x)   b'My name is St\xc3\xe5le'

#endswith()	Returns true if the string ends with the specified value
#Check if position 5 to 11 ends with the phrase "my world.":

txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)

print(x)   False

#expandtabs()	Sets the tab size of the string
#Set the tab size to 2 whitespaces:

txt = "H\te\tl\tl\to"

print(txt)        H       e       l       l       o
print(txt.expandtabs())      H       e       l       l       o
print(txt.expandtabs(2))    H e l l o
print(txt.expandtabs(4))        H   e   l   l   o
print(txt.expandtabs(10))      H         e         l         l         o


#find()	Searches the string for a specified value and returns the position of where it was found
#Where in the text is the first occurrence of the letter "e"?:
#If the value is not found, the find() method returns -1, but the index() method will raise an exception

txt = "Hello, welcome to my world."

x = txt.find("e", 5, 10)

print(x)   8

#format()	Formats specified values in a string
#Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:

txt = "For only {price:.2f} dollars!"

print(txt.format(price = 49))    For only 49.00 dollars!

#The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.

#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)   My name is John, I'm 36
print(txt2)   My name is John, I'm 36
print(txt3)   My name is John, I'm 36

#format_map()	Formats specified values in a string

#index()	Searches the string for a specified value and returns the position of where it was found
#Where in the text is the word "welcome"?:

txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)    7

#isalnum()	Returns True if all characters in the string are alphanumeric
#returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).

txt = "Company12"

x = txt.isalnum()

print(x)    True

txt = "Company 12"

x = txt.isalnum()

print(x)    False

#isalpha()	Returns True if all characters in the string are in the alphabet
#Check if all the characters in the text are letters:

txt = "CompanyX"

x = txt.isalpha()

print(x)  True

#isascii()	Returns True if all characters in the string are ascii characters
#Check if all the characters in the text are ascii characters:

txt = "Company123"

x = txt.isascii()

print(x)   True

#isdecimal()	Returns True if all characters in the string are decimals
#Check if all the characters in a string are decimals (0-9):

txt = "1234"

x = txt.isdecimal()

print(x)  True

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal()) True
print(b.isdecimal()) False

#isdigit()	Returns True if all characters in the string are digits
#Check if all the characters in the text are digits:

txt = "50800"

x = txt.isdigit()

print(x)

True

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())  True
print(b.isdigit())  True

#isidentifier()	Returns True if the string is an identifier
#Check if the strings are valid identifiers:
#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())  True
print(b.isidentifier())  True
print(c.isidentifier())  False
print(d.isidentifier())  False

#islower()	Returns True if all characters in the string are lower case
#Check if all the characters in the texts are in lower case:

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())   False
print(b.islower())   True
print(c.islower())   False

#isnumeric()	Returns True if all characters in the string are numeric
#returns True if all the characters are numeric (0-9), otherwise False. Exponents, like ² and ¾ are also considered to be numeric values."-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
#Check if the characters are numeric:

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())  True
print(b.isnumeric())  True
print(c.isnumeric())  False 
print(d.isnumeric())  False
print(e.isnumeric())  False

#isprintable()	Returns True if all characters in the string are printable
#Example of none printable character can be carriage return and line feed.
#Check if all the characters in the text are printable:

txt = "Hello!\nAre you #1?"

x = txt.isprintable()

print(x)   False

txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)   True

#isspace()	Returns True if all characters in the string are whitespaces
#Check if all the characters in the text are whitespaces:

txt = "   "

x = txt.isspace()

print(x)    True

txt = "   s   "

x = txt.isspace()

print(x)   False

#istitle()	Returns True if the string follows the rules of a title
#Check if each word start with an upper case letter:

txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x) true

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())     False
print(b.istitle())     True
print(c.istitle())     True
print(d.istitle())     True

#isupper()	Returns True if all characters in the string are upper case
#Check if all the characters in the text are in upper case:

txt = "THIS IS NOW!"

x = txt.isupper()

print(x)  True

a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())   False
print(b.isupper())   False
print(c.isupper())   True

#join()	Joins the elements of an iterable to the end of the string
#Join all items in a tuple into a string, using a hash character as separator:

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)   John#Peter#Vicky

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)   nameTESTcountry

#ljust()  Returns a left justified version of the string
#Return a 20 characters long, left justified version of the word "banana":

txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")  banana              is my favorite fruit.

#Using the letter "O" as the padding character:

txt = "banana"

x = txt.ljust(20, "O")

print(x)   bananaOOOOOOOOOOOOOO

#lower()	Converts a string into lower case
#Lower case the string:

txt = "Hello my FRIENDS"

x = txt.lower()

print(x)   hello my friends

#lstrip()	Returns a left trim version of the string
#Remove spaces to the left of the string:

txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")   of all fruits banana     is my favorite

#Remove the leading characters:

txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")

print(x)  banana

#maketrans()	Returns a translation table to be used in translations
#Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:

txt = "Hello Sam!"

mytable = str.maketrans("S", "P")

print(txt.translate(mytable))  Hello Pam!

#Use a mapping table to replace many characters:

txt = "Hi Sam!"

x = "mSa"
y = "eJo"

mytable = str.maketrans(x, y)

print(txt.translate(mytable))   Hi Joe!

#The third parameter in the mapping table describes characters that you want to remove from the string:

txt = "Good night Sam!"

x = "mSa"
y = "eJo"
z = "odnght"

mytable = str.maketrans(x, y, z)

print(txt.translate(mytable))   G i Joe!

#The maketrans() method itself returns a dictionary describing each replacement, in unicode:

txt = "Good night Sam!"

x = "mSa"
y = "eJo"
z = "odnght"

print(str.maketrans(x, y, z))   {97: 111, 83: 74, 100: None, 103: None, 104: None, 116: None, 109: 101, 110: None, 111: None}

#partition()	Returns a tuple where the string is parted into three parts
#Search for the word "bananas", and return a tuple with three elements:

#1 - everything before the "match"
#2 - the "match"
#3 - everything after the "match"

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)    ('I could eat ', 'bananas', ' all day')

#If the specified value is not found, the partition() method returns a tuple containing: 1 - the whole string, 2 - an empty string, 3 - an empty string:

txt = "I could eat bananas all day"

x = txt.partition("apples")

print(x)  ('I could eat bananas all day', '', '')

#replace()	Returns a string where a specified value is replaced with a specified value
#Replace the word "bananas":

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)   I like apples

#Replace all occurrence of the word "one":

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three")

print(x)    three three was a race horse, two two was three too.

#Replace the two first occurrence of the word "one":

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)    three three was a race horse, two two was one too.

#rfind()	Searches the string for a specified value and returns the last position of where it was found
#Where in the text is the last occurrence of the string "casa"?:

txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)    12

#Where in the text is the last occurrence of the letter "e"?:

txt = "Hello, welcome to my world."

x = txt.rfind("e")

print(x)    13

#Where in the text is the last occurrence of the letter "e" when you only search between position 5 and 10?:

txt = "Hello, welcome to my world."

x = txt.rfind("e", 5, 10)

print(x)   8

#If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception:

txt = "Hello, welcome to my world."

print(txt.rfind("q"))  -1
print(txt.rindex("q"))   not found

#rindex()	Searches the string for a specified value and returns the last position of where it was found
#Where in the text is the last occurrence of the string "casa"?:

txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)    12

#Where in the text is the last occurrence of the letter "e"?:

txt = "Hello, welcome to my world."

x = txt.rfind("e")

print(x)    13

#Where in the text is the last occurrence of the letter "e" when you only search between position 5 and 10?:

txt = "Hello, welcome to my world."

x = txt.rfind("e", 5, 10)

print(x)   8

#If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception:

txt = "Hello, welcome to my world."

print(txt.rfind("q"))  -1
print(txt.rindex("q"))   not found

#rjust()	Returns a right justified version of the string
#Return a 20 characters long, right justified version of the word "banana":

txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")         banana is my favorite fruit.

#Using the letter "O" as the padding character:

txt = "banana"

x = txt.rjust(20, "O")

print(x)    OOOOOOOOOOOOOObanana

#rpartition()	Returns a tuple where the string is parted into three parts
#Search for the last occurrence of the word "bananas", and return a tuple with three elements:

#1 - everything before the "match"
#2 - the "match"
#3 - everything after the "match"

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)   ('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')

#If the specified value is not found, the rpartition() method returns a tuple containing: 1 - an empty string, 2 - an empty string, 3 - the whole string:

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("apples")

print(x)   ('', '', 'I could eat bananas all day, bananas are my favorite fruit')

#rsplit()	Splits the string at the specified separator, and returns a list
#Split a string into a list, using comma, followed by a space (, ) as the separator:

txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)    ['apple', 'banana', 'cherry']

#Split the string into a list with maximum 2 items:

txt = "apple, banana, cherry"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)  

print(x)    ['apple, banana', 'cherry']

# note that the result has only 2 elements "apple, banana" is the first element, and "cherry" is the last.

#rstrip()	Returns a right trim version of the string
#Remove any white spaces at the end of the string:

txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")    of all fruits     banana is my favorite

#Remove the trailing characters if they are commas, periods, s, q, or w:

txt = "banana,,,,,ssqqqww....."

x = txt.rstrip(",.qsw")

print(x)    banana

#split()	Splits the string at the specified separator, and returns a list
#Split a string into a list where each word is a list item:

txt = "welcome to the jungle"

x = txt.split()

print(x)    ['welcome', 'to', 'the', 'jungle']

#Split the string, using comma, followed by a space, as a separator:

txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)   ['hello', 'my name is Peter', 'I am 26 years old']

txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)    ['apple', 'banana', 'cherry', 'orange']

#Split the string into a list with max 2 items:

txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)    ['apple', 'banana#cherry#orange']

#splitlines()	Splits the string at line breaks and returns a list
#Split a string into a list where each line is a list item:

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)   ['Thank you for the music', 'Welcome to the jungle']

#Split the string, but keep the line breaks:

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines(True)

print(x)    ['Thank you for the music\n', 'Welcome to the jungle']

#startswith()	Returns true if the string starts with the specified value
#Check if the string starts with "Hello":

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)    True

#Check if position 7 to 20 starts with the characters "wel":

txt = "Hello, welcome to my world."

x = txt.startswith("wel", 7, 20)

print(x)    True

#strip()	Returns a trimmed version of the string
#Remove spaces at the beginning and at the end of the string:

txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")    of all fruits banana is my favorite

#Remove the leading and trailing characters:

txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)    banana

#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#Make the lower case letters upper case and the upper case letters lower case:

txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)    hELLO mY nAME iS peter

#title()	Converts the first character of each word to upper case
#Make the first letter in each word upper case:

txt = "Welcome to my world"

x = txt.title()

print(x)   Welcome To My World

txt = "Welcome to my 2nd world"

x = txt.title()

print(x)     Welcome To My 2Nd World

#Note that the first letter after a non-alphabet letter is converted into a upper case letter:

txt = "hello b2b2b2 and 3g3g3g"

x = txt.title()

print(x)    Hello B2B2B2 And 3G3G3G

#translate()	Returns a translated string
#Replace any "S" characters with a "P" character:

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}

txt = "Hello Sam!"

print(txt.translate(mydict))    Hello Pam!

txt = "Hello Sam!"

mytable = str.maketrans("S", "P")

print(txt.translate(mytable))    Hello Pam!

#The same example as above, but using a dictionary instead of a mapping table:

txt = "Good night Sam!"

mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}

print(txt.translate(mydict))    G i Joe!

#upper()	Converts a string into upper case
#Upper case the string:

txt = "Hello my friends"

x = txt.upper()

print(x)   HELLO MY FRIENDS

#zfill()	Fills the string with a specified number of 0 values at the beginning
#Fill the string with zeros until it is 10 characters long:

txt = "50"

x = txt.zfill(10)

print(x)     0000000050

#Fill the strings with zeros until they are 10 characters long:

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))      00000hello
print(b.zfill(10))      welcome to the jungle
print(c.zfill(10))      000010.000
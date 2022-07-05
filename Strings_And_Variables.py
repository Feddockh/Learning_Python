# Both double and single quotes can be used to designate strings
print("String with double quotes")
print('String with single quotes')

# Escaping characters can be preformed by using a backslash \
print('Using Python\'s escape sequences')

# A newline can be created by using the newline escape sequence \n
print("This\nwill create a new line")

# A newline can also be created automatically by using three qoutations
print("""This 
will also create a new line""")

# Strings can be concatenated using +
print("Palm Beach" + "is close now")

# Strings can also be repeated when multiplied by an int
print("repeat " * 3)

# Variables do not require you to specify a datatype
example = "something"

# Variable names can contain letters, numbers, and underscores
# A variable name cannot begin with a number
example_2 = 2

# Use the input() function to take user input
x = input()
print(x)

# The input function can also prompt an input
x2 = input("Please enter an input: ")
print(x2)

# Input is always stored as a string, so we can convert data types using int(), float() functions
x3 = int(input("Please enter a number: "))

# In-place operators include +=, -=, *=, /=, %=
x3 += 1

# In-place operators also be used on strings
str1 = "Hello "
str1 += "there"
print(str1)

# Walrus Operator := allows you to assign values to variables within an expression, including variables that don't exist yet
print(num := int(input("Walrus Operator Int: ")))








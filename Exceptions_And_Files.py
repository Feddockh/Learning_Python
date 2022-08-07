# Exceptions occur when something goes wrong
#print(7/0)

# Different exceptions
# importError: an import fails
# IndexError: a list is indexed with an out-of-range number
# NameError: an unknown variable is used
# SyntaxError: the code can't be parsed properly
# TypeError: a function is called on a value of an inappropriate type
# ValueError: a function is called on a value of the correct type, but with an inappropriate value

# Use a try/except statement to handle exceptions, and call code when one occurs
# A try statement can have multiple exceptions
# Multiple exceptions can also be put into a single exception block using parenthesis
# The finally statement always runs after the code in try and except blocks regardless of any caught or uncaught exceptions
from calendar import firstweekday


try:
    num1 = 7
    num2 = 0
    print (num1 / num2)
    print("done calculation")
except ZeroDivisionError:
    print("An error has occured due to zero division")
except (ValueError, TypeError):
    print("An error has occured due to a value or type error")
finally:
    print("This code will run regardless of any exceptions")
# an except statement without any exception specified will catch all errors and should be used sparingly

# Exceptions can be raised using the raise statement followed by the exception type
# Exceptions can be raised with arguments that give detail about the exception
num = 1
try:
    if num == 1:
        raise ValueError("num can't be 1") # This exception's arguments would display if it was outside of this try/except block
except ValueError:
    print("The ValueError exception was raised")
# In the except block, the raise statement can be used with no arguments to re-raise whatever exception occured

# assert statements can be used to test expressions and if the result comes up false, an AssertionError exception is raised
# The assert can take a second argument that gives details about the AssertionError raised
temp = -10
try:
    assert (temp >= 0), "Colder than absolute zero"
except AssertionError:
    print("Assertion false")

# The open function can be used to open files
# If the file is in the current directory you can specify just the name
# You can specify the mode used to open a file by applying a second argument
    # "r" opens in read mode, which is the default mode
    # "w" opens in write mode, for rewriting the contents of the file
    # "a" opens in append mode, for adding new contents to the file
    # Adding a "b" after the mode opens it in binary mode (used for non-text files such as images or audio files)
    # You can use the + sign with each mode to give extra access to a file
# Read mode (default)
myfile = open("filename.txt", "r")
# Write mode
myfile = open("filename.txt", "w")
# Binary read mode
myfile = open("filename.txt", "rb")
# Read and write mode
myfile = open("filename.txt", "r+")
# Once the file is openned and used, you should close it with the close() method
myfile.close()

def resetMyFile():
    myfile = open("filename.txt", "w")
    myfile.write("Hello this is a test\nThis is line 2")
    myfile.close()

# The read() function can be used to read some or all of the files contents
    # If an argument is given to the function it specifies the number of bytes read
    # You can store the data from the file to a variable, or you can just print directly
    # Once all the contents in the file have been read, any further attempts to read further will return an empty string
resetMyFile()
myfile = open("filename.txt")
firstWord = myfile.read(6)
print(firstWord)
print(myfile.read())
myfile.close()

# The readlines() function can be used to return a list in which each element in the list is from a different line in the file
resetMyFile()
myfile = open("filename.txt")
print(myfile.readlines())
myfile.close()

# A for loop can also be used to iterate through lines in a file
resetMyFile()
myfile = open("filename.txt")
for line in myfile:
    print(line)
myfile.close()

# The write() function can be used to write to a file once it has been openned
    # When a file is openned in write mode, a new file is made and existing data with that filename is overwritten
    # The write() method returns the number of bytes written to a file if successful
    # Only strings can be written, so other types will have to be converted
myfile = open("filename.txt", "w")
myfile.write("I am writing to a file now")
print(myfile.write("This should return 21")) # The len() function can be used instead here to validate
myfile.close()

# Writing files challenge
names = ["John", "Oscar", "Jacob"]
file = open("filename.txt", "w+") # Why "w+"?
# Write the names into the file on different lines
for i in names: # Using a for loop that iterates through the list
    file.write(i + "\n")
file.close()
file= open("filename.txt", "r")
# Ouput the contents of the file
print(file.read()) 
file.close()

# Using try and finally to make sure that files are always closed after use
    # This ensures that the file always closed even if an error occurs
resetMyFile()
try:
    myfile = open("filename.txt")
    print(myfile.read())
finally:
    myfile.close()

# A cleaner way to ensure that files are safely closed is using a with statement
    # Creates a temporary variable for accessing the file only within the with statement block
    # This file is automatically closed at the end of the statement even if exceptions occur within
resetMyFile()
with open("filename.txt") as myfile:
    print(myfile.read())

with open("filename.txt") as f:
    text = f.read()
print(text)



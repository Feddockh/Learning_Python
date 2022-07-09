# Use the def statement to create functions
# Code block of the function begins with a colon : and is indented
def my_func():
    print("Hello")
my_func() # Calling the function
# You have to define functions before calling them

# Define arguments of a function by putting them in the parenthesis
def sum(x, y):
    print(x + y)
sum(1, 2)
# Function parameters cannot be referenced outside of the function's definition

# The return statement can be used to return a value from a function
# Once a value is returned, the function immediately stops
def getSum(x, y):
    return x + y
ans = getSum(1, 2)
print(ans)

# Comments and Docstrings
# Comments use a hash symbol, there are no multiline comments like C
""" Docstrings are specifically for explaining code and usually exist below the functions first line """

# Functions can be assigned and reassigned to variables
newGetSum = getSum
print(newGetSum(1, 2))

# Functions can also be used as arguments of other functions
def twice(func, x, y):
    return func(func(x, y), func(x, y))
print(twice(getSum, 1, 2))

# Modules contain functions and variables and can be imported
import random # Should go at top of code
# Module functions and variables can be accessed through the module
x = random.randint(1, 6)

# Another way to import only certain functions from a module
# A comma seperated list can be used to import multiple objects
# Just using import, imports everything from a module and is usually discouraged because it confuses variables in code with variables in your module
from math import pi, sqrt
# Trying to import a module that isn't available causes an import error

# You can import a module under a different name using the as keyword
# Usually used with long/confusing names
from math import sqrt as square_root
print(square_root(100))

# The three main types of modules in python are those that you write, those you install from external sources, and those that are preinstalled with python
# The standard library is preinstalled with python
# The standdard library includes modules string, re, datetime, math, random, os, mutliprocessing, subprocessing, socket, email, json, doctest, unittest, pdb, argparse, and sys
# Some of the modules in the standard library are written in python and some are written in C
# The complete documentation for the standard library can be found at www.python.org

# Many third-party modules are stored on the Python Package Index (PyPI)
# The best way to install these is using a program called pip
# Usually pip is installed with the python package
# Look up the name of the library and enter pip install library_name in the command line/prompt




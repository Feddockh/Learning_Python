# Functional programming takes advantage of higher-order functions 
    # higer-order functions either take functions as arguments or return them 

def test(func, arg):
    return func(func(arg))
def mult(x):
    return x*x
print(test(mult, 2))
    
# Pure functions return values that depend only on their arguments
    # Ideal for functional programming (ex. sin and cos)

# Using lambda syntax allows you to make functions on the fly
    # lambda (args): (expression)
    # Usually used when passing a simple function as an argument to another function
    # Functions created this way are called "anonymous functions"
def func(f, arg): # Function takes function f and arg and returns f(arg)
    return f(arg)
func(lambda x: 2*x*x, 5) # Passing a lambda function to the func function

# You can also call the lambda function with an argument right after making it
    # Format: argument surrounded by parenthesis like normally passing arguments
print((lambda x: x**2 + 5*x + 4) (-4))

# You can also assign lambda functions to variables
    # Not recommended, using def is better for defining functions
double = lambda x: x*2
print(double(2))

# The map and filter functions are higher-order functions that operate on lists (or iterables)

# map() - Applies a function to all items in an iterable
    # Format: map(function, list)
    # The map function has to be converted to a list (using list()) if you want to print it
def add_five(x):
    return x + 5
nums = [10, 20, 30, 40, 50]
result = list(map(add_five, nums)) # list() has to be used to convert from map object (weird format)
print(result)
# We could also use the lambda syntax
result = list(map(lambda x: x + 5, nums))
print(result)

# filter() - Removes items from an iterable that don't match a predicate (function that returns a boolean)
    # Format: filter(predicate, list)
nums = [11, 22, 33, 44, 55]
result = list(filter(lambda x: x%2==0, nums)) # list() function also used to make filter() data printable
print(result)

# Generators allow you to declare a function that behaves like an iterator (i.e. usually used in a for loop)
    # Like a list or turple, but doesn't allow arbitrary indicies
    # Defined using a function and a yield statement
# The yield statement replaces the return statement to provide a result without destroying local variables
    # Basically "yields" the variable value at that point without actually returning from the function
def countdown():
    i=5
    while i>0:
        yield i
        i -= 1
for i in countdown(): # i is an iterable in countdown()
    print(i) # The yield statement is returning this value to be printed each iteration
    
# Since generators yield one item at a time, they don't have the memory restriction of lists (they can be infinite)
#def infinite_sevens():
#  while True:
#    yield 7
#for i in infinite_sevens():
#  print(i)

# Finite generators can be converted to lists by passing them through list()
def numbers(x):
    for i in range(x):
        if i%2==0:
            yield i
print(list(numbers(11)))
    # Using generators improves performance because the on demand generation of values results in lower memory usage
    # Additionally, we don't have to wait for all the elements to be generated before we use them

# Practice: Split Generator
txt = "This is a test" # Takes sentence input
def words():
    txtSep = txt.split(" ") # Splits sentence into words
    for i in txtSep: # Iterates through the words
        yield i # yields each word as it iterates
print(list(words())) # prints out the result of the finite generator after converting to a readable list()

# Decorators provide a way to modify functions with other functions
def decor(func): # decor() decorates a text function
  def wrap(): # wrap() prints the decorations and calls the passed func() and returns wrap()
    print("============")
    func()
    print("============")
  return wrap
def print_text():
  print("Hello world!")
print_text = decor(print_text) # Reassigning the print_text function to include the decorated version
print_text() # Calling the print_text function, and it now corresponds to our decorated function

# Alternatively we could also use the @ symbol with the decorating function name followed by the definition of the decorated name
@decor
def print_text2():
    print("Hello world 2!")
print_text2()

# Recursion is the act of using functions that reference themselves to break down a problem into sub problems of the same type
    # The base case acts as the exit condition of the recursion and does not call the function again
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(5))

# Recursive functions can be infinite without the base case
    # This usually results in the program running out of memory and crashing
# Recursion can also be indirect, one function can call the second, which calls the first, etc.

# Practice: sum of squares of all x list items
def calc(x):
    if len(x)==0:
        return 0
    else:
        return x[0]**2 + calc(x[1:]) 
x = [1, 3, 4, 2, 5]
sum = calc(x)        
print(sum)

# Sets are data structures, similar to lists or dictionaries, created with {} or set()
    # They share some functionality with lists, such as the use of the in statement to check contents
    # To create an empty set you have to use set(), using {} makes an empty dictionary
num_set = {1, 2, 3, 4, 5} # Used curly brackets here
word_set = set(["spam", "eggs", "sausage"]) # Used set() here
print(3 in num_set)
print("spam" not in word_set)
# Comparision between sets and lists
    # Both sets and lists share the len()
    # Sets are unordered, and therefore can't be indexed
    # Sets cannot contain duplicate elements
    # Due to the way it is stored, it is faster to check whether an item is part of a set than a list
    # append() is used to add to a list, add() is used to add to a set
    # remove() removes a specific element from a set, pop() removes an arbitrary element
# Basic uses of sets include membership testing and elimination of duplicate entries

# Sets can be combined using mathematical operations
    # Union operator | combines two sets to form a new one
    # Intersection operator & gets items only in both
    # Difference operator - gets items in the first set, but not the second
    # Symmetric Difference operator ^ gets items in either set, but not both
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

# Python data structures: lists, dictionaries, tuples, sets
    # Use a dictionary when you want a key:value pair, fast lookup, and potential modification
    # Use a list if you do not need random access to data, but want a simple, iterable, and modifiable collection of data
    # Use a set if you need uniqueness for each element
    # Use tuples when your data cannot change
        # Oftentimes a tuple may represent the keys in a dictionary 

# itertools is a standard library that contains several useful functions
import itertools
    # count() - counts up infinitely from a value
for i in itertools.count(3):
    print(i)
    if i >= 11:
        break
    # cycle() - Indefinitely iterates through an iterable (for instance a list or string)
    # repeat() - Repeats an object either indefinitely or a specific number of times
    # takewhile() - Takes items from an iterable while a predicate (true/false) function remains true
    # chain() - Combines several iterables into one long one
    # accumulate() - Returns a running total of values in an iterable
nums = list(itertools.accumulate(range(8)))
print(nums)
print(list(itertools.takewhile(lambda x: x<= 6, nums)))
# Combinatoric functions accomplish a task with all possible combinations of some items
    # product() - Produces all possible combinations of the inputs
    # permutations() - Produces all arrangements of the input
letters = ("A", "B")
print(list(itertools.product(letters, range(2))))
print(list(itertools.permutations(letters)))


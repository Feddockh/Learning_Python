# The None object is similar to null represents the absence of a value
print(None)

# Dictionaries are data structures that map arbitrary keys to values
    # Lists can be throught of like dictionaries with integer keys within a set range
    # Dictionaries are made with {} whereas lists are made with []
emptyDictionary = {}
    # Each element in a dictionary is represented by a key:value pair
roommates = {"Eric":22, "Austin":22, "Liming":28}
print(roommates["Eric"])
print(roommates["Liming"])

# Trying to index a nonexistent key returns a KeyError
try:
    print(roommates["Keegan"])
except KeyError:
    print("KeyError caught")

# Keys must be an immutable object (ex. not lists or dictionaries)
    # Trying to use a mutable object causes a TypeError

# The dictionary get() method does the same thing as indexing, but prevents KeyErrors
    # If the key doesn't exist, it returns None by default
    # First parameter is the key, second parameter is the value to return upon failure
nums = {1:57, 3:45, 5:50}
print(nums.get(1))
print(nums.get(5))
print(nums.get(7, "7 is out of the range"))

# Tuples are immutable (unchangable) lists
    # These are created with () instead of {} or []
    # Tuples can also be created without the () and just commas to seperate values
    # They are faster to access than lists, but cannot be reassigned
sampleTuple = ("This", "is", "a", "tuple")
print(sampleTuple[3])
# Trying to reassign values in a tuple causes a TypeError
try:
    sampleTuple[1] = "can't Reassign Tuple"
except TypeError:
    print("TypeError caught")
# Like lists and dictionaries, tuples can also be nested within each other
tpl = (1, (1, 2, 3))
print(tpl[1])

# List slicing allows you to return a portion of an existing list
    # Format: [start:end:step] (although the step argument can be omitted)
    # List slicing can also be done on tuples
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[2:8:3])
    # Note: Like range, the first indexed value is included and the second is not
    # Note: sList indexing does begin with 0
# Omitting the first or second number assumes the front or end of the list
print(squares[:7])
print(squares[7:])
print(squares[1::4])
# Negative values will count from the back of the list
    # If a negative value is used for the step, the slice is done backwards
print(squares[1:-1]) # Same as [1:9]
print(squares[::-1]) # This is a common way to reverse a list

# List comprehensions create lists with rules
    # Inspired by set-builder notation in mathematics
cubes = [i**3 for i in range(5)]
# Can also contain an if statement to enforce a condition
evens = [i**2 for i in range(10) if i**2 % 2 == 0]
# Trying to create a list with a large range will result in a MemoryError
    # Issue is solved by using generators, which we learn later
    # Example: even = [2*i for i in range(10**10000)]
    
# String formatting is a more powerful way to embed non-strings within strings
    # As opposed to converting datatypes and then adding then together
    # Uses a string's format method which places each argument in the coresponding position
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)
    # Note: Notice there is a period after the string, not a comma
# String formatting can also use named arguments
a = "Point a = {x}, {y}".format(x=5, y=12)
print(a)

# String functions
# join - joins a list of stings with another string as a seperator
print(", ".join(["spam", "eggs", "ham"]))
# replace - replaces one substring in a string with another
print("Hello test".replace("test", "World"))
# startswith/endswith - determines if there is a substring at the start/end of a string
print("Where is Eric and Austin".startswith("Where"))
print("Where is Eric and Austin".endswith("Austin"))
# lower/upper - changes text case
print("Where is Eric and Austin".lower())
print("Where is Eric and Austin".upper())
# split - opposite of join, turns a string with a certain seperator into a list
print("spam, eggs, ham".split(", "))

# Numeric functions
# max and min - returns the max/min value in a list
print(min([1, 2, 3, 4, 5, 6]))
print(max([1, 2, 3, 4, 5, 6]))
# abs - returns the numbers absolute value
print(abs(-7))
# round - rounds a number to a certain number of decimal places
print(round(1.787))
# sum - returns the total of a list
print(sum([1, 2, 3, 4, 5, 6]))

# List functions
# all and any - returns true if all/any of thier arguments evaluate to true
nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):
    print("All larger than 5")
if any([i % 2 == 0 for i in nums]):
    print("At least one is even")
# enumerate - can be used to simultaneously iterate through all list values
for v in enumerate(nums):
    print(v)






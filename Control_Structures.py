# Boolean values are True and False
b = True
print(b)

# Booleans can also be created using comparative operators ==, !=, >, <, >=, <=
print(2 == 3)

# if statements use indentation to designate content inside the operator
# colons are used after the expression (don't forget!)
# else if is designated with elif
if 10 < 5:
    print ("10 is less than 5")
elif 10 > 5:
    print("10 is greater than 5")
else:
    print ("Otherwise")
print("Program ended")

# Python's boolean operators include and, or, and not
print (1 == 1 and 2 == 2)

# Python's order of operations is math operators, comparative operators, and then boolean operators
print (1 + 0 > 0 and True)

# Lists are created using square brackets with commas seperating items
# Lists are zero-indexed
# You can leave a comma after the last entry in the list if you want
words = ["I", "am", "at", "the", "beach"]
print(words[0])
print(words[4])
print(words)

# You can create an empty list (pointer) and populate it later using empty brackets
emptyList = []
print(emptyList)

# Lists can include several different types
# Lists can also be nested in other lists
things = ["string", 0, [1, 2], 4.56]
print(things[2])
print(things[2][1])

# Nested lists can be used to represent 2D lists (matricies)
m = [ 
    [1, 2, 3],
    [4, 5, 6]
    ]
print ("5 =", m[1][1])

# Strings can also be treated as character lists
str = "Beach Time"
print("T =", str[6])

# List values can be reassigned
nums = [7, 7, 7, 7]
nums[2] = 5
print(nums)

# Addition and subtraction can be applied to lists
print(nums + [4, 5, 6])
print(nums * 2)

# Use the in operator to check if an item is in a list
# Not operator can be used in either of the following ways
nums2 = [2, 2, 2]
print(2 in nums2)
print(not 3 in nums)
print(3 not in nums)

# The append() function can be used to add items to the end on an existing list
# This function is a method of the list class
nums3 = [1, 2, 3]
nums3.append(4)
print(nums3)

# The len() function returns the number of items in a list
print(len(nums))

# The insert() function allows you to insert an item at any position in the list
# This function is a method of the list class
# Elements after the inserted item are shifted right
nums3.insert(1, 10)
print(nums3)

# The index() function finds the first occurrance of an item in a list
# Returns a ValueError if the item does not exist in the list
# This function is a method of the list class
print(nums3.index(2))

# Other helpful list functions 
# max() and min() functions return a list item with the max/min value
print(max(nums3))
print(min(nums3))
# count() returns the number of occurances of an item in a list
print(nums3.count(1))
# remove() removes an object from a list
nums3.remove(10)
print(nums3)
# reverse() reverses the order of items in a list
nums3.reverse()
print(nums3)

# statements within the while loop are indented
# Remember the colons after the while condition
i = 1
while i <= 5:
    print(i)
    i += 1
print("done")

# break can be used to stop a while loop
# Using break outside of a loop causes an error
i = 1
while True:
    if i > 5:
        break
    print(i)
    i += 1
# continue can be used to jump back to the top of a loop





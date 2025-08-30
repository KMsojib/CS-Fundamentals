"""
Array Lesson for Junior Students
-------------------------------

What is an Array?
-----------------
An array is a collection of items stored at contiguous memory locations. 
The idea is to store multiple items of the same type together.

In Python, arrays are usually represented using lists.

Why use Arrays?
---------------
- To store multiple values in one variable.
- To process collections of data efficiently.

Creating Arrays (Lists)
-----------------------
"""

# Create an array of numbers
numbers = [1, 2, 3, 4, 5]
print("Numbers array:", numbers)

# Create an array of strings
fruits = ["apple", "banana", "cherry"]
print("Fruits array:", fruits)

"""
Accessing Array Elements
------------------------
"""

print("First number:", numbers[0])  # Output: 1
print("Second fruit:", fruits[1])   # Output: banana

"""
Changing Array Elements
-----------------------
"""

numbers[2] = 10
print("Changed numbers array:", numbers)  # [1, 2, 10, 4, 5]

"""
Array Operations
----------------
"""

# Add an item to the end
fruits.append("orange")
print("Fruits after append:", fruits)

# Remove an item
fruits.remove("banana")
print("Fruits after remove:", fruits)

# Get length of array
print("Length of numbers array:", len(numbers))

"""
Looping through Arrays
----------------------
"""

print("Looping through numbers:")
for number in numbers:
    print(number)

"""
Useful Array Methods
--------------------
"""

# Sorting an array
numbers.sort()
print("Sorted numbers:", numbers)

# Reversing an array
fruits.reverse()
print("Reversed fruits:", fruits)

"""
Common Array Mistakes
---------------------
- Indexing starts at 0, not 1!
- Accessing an index out of range causes an error.
"""

# Uncommenting the following line will cause an error
# print(numbers[10])  # IndexError

"""
Practice Exercises
------------------
1. Create an array of your three favorite colors and print it.
2. Add another color to your array and print it.
3. Remove the first color from your array and print it.
4. Print each color using a loop.
5. Sort the colors array and print it.
"""

# You can try these exercises below!

"""
Extra: Arrays in Other Languages
-------------------------------
In other languages like Java or C, arrays have fixed size and only store one type.
Python lists are more flexible.

References
----------
- https://www.w3schools.com/python/python_lists.asp
- https://www.programiz.com/python-programming/list
"""

# End of Lesson
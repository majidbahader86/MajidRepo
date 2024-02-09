# what are linear collections 
# Linear collections refer to data structures that organize elements in a sequential manner, allowing access to elements in a linear sequence. 

# Lists 
# lists are mutable, ordered collections that contain elements of different types. We can add, remove or modify elements in a list. 

#my_list = [1, 2, 3, 'apple', 'banana', True]
"""
# accessing elements 
print(my_list[0])
print(my_list[3])
# Modifying elements 
my_list[1] = "orange"
print(my_list)
# adding elements 
my_list.append(10)
print(my_list)
# removing elements
my_list.remove(3)
print(my_list)"""
# To ensure that 'True' is removed only from the end of the list, one can remove slicing to remove the last element 
#my_list = my_list[:-1]
#my_list = my_list[2:4]
#my_list = my_list[2:]
#print(my_list)

# using a for loop
#for item in my_list:
    #print(item)

# The sort() method sorts the elements of a list in ascending order. When you execute the code:
#my_list = [3, 2, 1]
#my_list.sort()
#print(my_list)

# dir(my_list) on a list object my_list, it will return a list of all the attributes and methods that can be used with lists in Python.
#print(dir(my_list))

# Packing and unpacking in python
# Packing: it refers to combining multiple values into  single data structure like a tuple or a list. 
# Example
my_tuple = 1, 2, 3  # Packing three values into a tuple
print(my_tuple)  # Output: (1, 2, 3)

#Unpacking: It refers to extracting individual values from a data structure like a tuple or a list.

#Example of unpacking:
my_tuple = (1, 2, 3)  # Tuple with three values
a, b, c = my_tuple  # Unpacking the tuple into individual variables
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Similarly, you can pack and unpack values with lists:

my_list = [4, 5, 6]  # List with three values
x, y, z = my_list  # Unpacking the list into individual variables
print(x)  # Output: 4
print(y)  # Output: 5
print(z)  # Output: 6
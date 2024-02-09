# what are linear collections 
# Linear collections refer to data structures that organize elements in a sequential manner, allowing access to elements in a linear sequence. 

# Lists 
# lists are mutable, ordered collections that contain elements of different types. We can add, remove or modify elements in a list. 

my_list = [1, 2, 3, 'apple', 'banana', True]
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

my_list.sort()
# Sets in Python

# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Sets automatically remove duplicate elements
my_set_with_duplicates = {1, 2, 2, 3, 3, 4, 5}
print("Set with Duplicates:", my_set_with_duplicates)

# Creating an empty set
empty_set = set()
print("Empty Set:", empty_set)

# Converting list to set
my_list = [1, 2, 3, 4, 5, 5]
converted_set = set(my_list)
print("Converted Set from List:", converted_set)

# Adding elements to a set
my_set.add(6)
my_set.add(7)
print("Set after Adding Elements:", my_set)

# Removing an element from a set
my_set.remove(5)
print("Set after Removing Element:", my_set)

# Set Operations

# Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of Sets:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection of Sets:", intersection_set)

# Difference
difference_set = set1.difference(set2)
print("Difference of Sets:", difference_set)

# Checking if element is in set
print("Is 3 in set1?", 3 in set1)
print("Is 6 in set1?", 6 in set1)

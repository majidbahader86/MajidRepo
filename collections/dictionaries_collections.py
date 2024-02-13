# Dictionaries in Python

# Define a dictionary
dict_1 = {'key1': 'value1', 'key2': 'value2'}

# Dictionaries have order
print(dict_1)

# Dictionaries allow duplicates in values
dict_2 = {'key1': 'value1', 'key2': 'value2'}

print(dict_2)

# Access value by key
print(dict_2['key2'])

# Dictionaries allow objects of different types
dict_3 = {1: 'value1', 'key2': 2, 'is_true': True}

print(dict_3)

# Convert nested tuple into dictionary
nested_tuple = (('name', 'pawl'), ('country', 'Germany'))
tuple_to_dict = dict(nested_tuple)

print(tuple_to_dict)

# Create empty set
new_set = set()

# Create empty dictionary
new_dict_2 = {}

# Create dictionary using dict constructor/keyword
new_dict = dict()

# Create a dictionary with boolean object as key
dict_4 = {True: 'yes', False: 'No'}

print(dict_4)

# Use fromkeys method to define dictionary
dict_5 = dict.fromkeys(('name', 'age', 'city', 'country'))

print(dict_5)

# Get value from dictionary using keys
print(dict_5['name'])

# Add value to a key in dictionary
dict_5['name'] = 'Alex'

print(dict_5['name'])

# Copy a dictionary using copy keyword
dict_6 = dict_5.copy()

print(dict_6)

# Update the dictionary with more key-value pairs
dict_6.update({'field': 'IT'})

print(dict_6)

# Get value using key indexing
print(dict_6['name'])

# Get value using get method
print(dict_6.get('name'))

# Modify value using key indexing
dict_6['name'] = 'Nina'

# print(dict_6)

# Check if key exists before accessing its value
'''
if dict_7.get('address'):
    print('value exist')
else:
    dict_7['address'] = 'Berlin, Germany'
    print('address key was not in dict, we added this key')
'''

# Remove dictionary item

# Dictionaries in Python are mutable, unordered collections of key-value pairs. They are used to store data in the form of key-value mappings, where each key is unique within the dictionary and associated with a corresponding value. Here's an overview of dictionaries in Python:

#Defining a Dictionary: Dictionaries are defined using curly braces {} and consist of key-value pairs separated by commas. Keys and values can be of any data type, but keys must be immutable (e.g., strings, numbers, tuples), while values can be mutable or immutable.


#my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 123}
#Accessing Values: Values in a dictionary are accessed using their corresponding keys. If a key is not present in the dictionary, it raises a KeyError.

#print(my_dict['key1'])  # Output: 'value1'
#Adding and Modifying Values: You can add new key-value pairs to a dictionary or modify existing values by assigning a new value to a key.

#my_dict['new_key'] = 'new_value'  # Adding a new key-value pair
#my_dict['key2'] = 'updated_value'  # Modifying an existing value
#Removing Items: You can remove items from a dictionary using the del keyword, pop() method, or popitem() method.

#del my_dict['key1']        # Remove a specific key-value pair
#my_dict.pop('key2')        # Remove and return the value for a specific key
#my_dict.popitem()          # Remove and return the last inserted key-value pair

#Dictionary Methods: Python provides various methods to perform operations on dictionaries, such as keys(), values(), items(), update(), clear(), copy(), get(), setdefault(), etc.

#keys = my_dict.keys()       # Get a list of all keys
#values = my_dict.values()   # Get a list of all values
#items = my_dict.items()     # Get a list of all key-value pairs
#my_dict.update({'key4': 'value4'})  # Update the dictionary with new key-value pairs

#my_dict.clear()             # Remove all items from the dictionary

#Nested Dictionaries: Dictionaries can contain other dictionaries as values, allowing you to represent hierarchical data structures.


#nested_dict = {'person': {'name': 'John', 'age': 30, 'city': 'New York'}}

#Dictionary Comprehensions: Similar to list comprehensions, dictionary comprehensions allow you to create dictionaries in a concise manner.


#squares = {x: x*x for x in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#Dictionaries are widely used in Python for tasks such as representing JSON data, caching values, mapping keys to values, and more. They provide a flexible and efficient way to store and manipulate data in Python programs.






# In Python, ChainMap is a data structure provided by the collections module that encapsulates multiple dictionaries into a single mapping.

# Example 

from collections import ChainMap

# Define dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Create a ChainMap
chain_map = ChainMap(dict1, dict2)

# Access keys
print(chain_map['a'])  # Output: 1
print(chain_map['b'])  # Output: 2 (from dict1)
print(chain_map['c'])  # Output: 4

# Update values
chain_map['b'] = 5
print(chain_map['b'])  # Output: 5 (updated in dict1)

# Add new key-value pair
chain_map['d'] = 6
print(chain_map['d'])  # Output: 6 (added to dict1)

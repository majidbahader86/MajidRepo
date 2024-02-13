# Statement: An instruction given to the Python interpreter.
# Example: Print statement and variable assignment statement.
print('DCI')  # This is a print statement
name = 'Pawl'  # This is another statement

# Expression: A value or combination of value and operators.
# Examples: 3, 1+2
3  # This is an expression
1 + 2  # This is another expression

# Loops:
# A loop is a way to execute/run Python statements multiple times.
# Python has two types of loops: for and while.

# For Loop:
# Used when the number of iterations is known.
# Example: Printing numbers from 0 to 9 using a for loop.
for x in range(10):
    print(x)

# While Loop:
# Used when the number of iterations is unknown but determined by a condition.
# Example: Printing numbers from 1 to 5 using a while loop.
number = 5
start_point = 1
while start_point <= number:
    print(start_point)
    start_point += 1

# Iterable and Iterator:
# An iterable is an object that consists of more than one value.
# An iterator is an object that knows its next state.

# Iterable Example:
name_iterable = 'DCI'  # It is an iterable

# Iterator Example:
name_iterator = iter(name_iterable)  # Convert iterable to iterator
print(next(name_iterator))  # Prints 'D'
print(next(name_iterator))  # Prints 'C'
print(next(name_iterator))  # Prints 'I'

# While Loop (One-liner):
# Example: Decrementing a number until it becomes 0 using a one-liner while loop.
number = 3
while number > 0: number -= 1; print(number)

# For Loop:
#A for loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each element in the sequence.

# Example 1: Iterating over a list
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5

# Example 2: Iterating over a string
message = "Hello"
for char in message:
    print(char)

# Output:
# H
# e
# l
# l
# o

# While Loop:
#A while loop is used to repeatedly execute a block of code as long as a specified condition is true.
    
# Example 1: Counting from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1

# Output:
# 1
# 2
# 3
# 4
# 5

# Example 2: Summing numbers until the sum reaches 100
total = 0
num = 1
while total < 100:
    total += num
    num += 1

print("Sum:", total)

# Output:
# Sum: 105

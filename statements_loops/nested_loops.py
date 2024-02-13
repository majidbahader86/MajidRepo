# Nested loops refer to a situation where you have one loop inside another loop. This allows you to iterate over multiple levels of data structures, such as lists of lists or matrices. Each iteration of the outer loop triggers the inner loop to execute its iterations.

# Here's a simple example to illustrate nested loops:

# Nested loop to print a multiplication table
for i in range(1, 6):  # Outer loop for rows
    for j in range(1, 11):  # Inner loop for columns
        print(i * j, end="\t")  # Print product of row and column
    print()  # Move to the next row after printing all columns

# in this example:

#The outer loop iterates over the rows from 1 to 5.
#The inner loop iterates over the columns from 1 to 10.
#Within the inner loop, it prints the product of the current row and column, followed by a tab character (\t).
#After printing all columns for a row, it moves to the next line using print().

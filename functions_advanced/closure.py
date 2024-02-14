def make_multiplier(factor):
    def multiplier(n):
        return n * factor
    return multiplier

# Create two multiplier functions with different factors
multiply_by_2 = make_multiplier(2)
multiply_by_3 = make_multiplier(3)

# Use the multiplier functions
result1 = multiply_by_2(5)  # result1 = 5 * 2 = 10
result2 = multiply_by_3(5)  # result2 = 5 * 3 = 15

print(result1)  # Output: 10
print(result2)  # Output: 15

# We define a function make_multiplier that takes a factor argument and returns another function multiplier.
# 1. Inside make_multiplier, multiplier is defined to accept a number n and return the result of n multiplied by factor.
# 2. When we call make_multiplier(2), it returns a function that multiplies its input by 2. We assign this function to multiply_by_2.
# 3. Similarly, when we call make_multiplier(3), it returns a function that multiplies its input by 3. We assign this function to multiply_by_3.
# 4. When we call multiply_by_2(5), it multiplies 5 by 2, resulting in 10.
# 5. When we call multiply_by_3(5), it multiplies 5 by 3, resulting in 15.
# In this way, the inner function multiplier remembers the value of factor even after the outer function make_multiplier has finished executing. This is an example of a closure in Python.

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure_example = outer_function(10)
result = closure_example(5)  # This will return 10 + 5 = 15

#In this example, inner_function forms a closure over the variable x from the outer scope of outer_function. The closure_example function retains access to the value of x (which is 10) even after outer_function has finished executing. When we call closure_example(5), it adds 5 to the value of x (which is 10), resulting in 15.

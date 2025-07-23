city = "Bangalore"  # Setting city as 'Bangalore'. This is an example of single line inline comment.
print(f"The city I will ever be greatful is: {city}");

"""
Python does not have multi line comments.
As a workaround, in the industry, a block enclosed within triple quotes is used as a multi line comment.

This content is not actually ignored on interpretation by the interpreter like comments, it gets interpreted and is treated as a multi line string literal.
In the code below, I update the city to Seattle and then print the city.
"""

city = "Seattle"
print(f"The city that I will work extremely hard to be in again is: {city}")
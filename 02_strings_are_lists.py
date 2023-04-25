
my_name = "Brutal Tröggh"

first_initial = my_name[0]

print(first_initial)

"""
####################  theory  ########################
Introduction to Strings
They're all Lists!

A string can be thought of as a list of characters.

Like any other list, each character in a string has an index. Consider the string:
"""
favorite_fruit = "blueberry"
"""
We can select specific letters from this string using the index. Let’s look at the first letter of the string.
"""
print(favorite_fruit[1])
# Output: l
"""
Whoops, is that the first letter you expected? Notice that the letter at index 1 of "blueberry" isn’t b, it’s l. This is because the indices of a string start at 0. b is located at the zero index and we could select it using:
"""
print(favorite_fruit[0])
# Output: b
"""
It’s important to note that indices of strings must be integers. If we were to try to select a non-integer index we would get a TypeError.

For example:
"""
print(favorite_fruit[1.5])
"""
This would result in:

Traceback (most recent call last):
  File "script.py", line 3, in <module>
    print(favorite_fruit[1.5])
TypeError: string indices must be integers

Instructions
1.

One of the most common things that are represented by strings is names.

Save your name as a string to the variable my_name.

Remember, the string can include more than one word:
"""
my_name = "Python Person"
"""
2.

Select the first letter of the variable my_name and save it to first_initial.

The first character of a string is at index 0:
"""
first_initial = my_name[0]
"""
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    In Python, what is a character?

Still have questions? View this exercise's thread in the Codecademy Forums.
"""

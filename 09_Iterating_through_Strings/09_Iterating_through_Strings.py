"""

Introduction to Strings
Iterating through Strings

Now you know enough about strings that we can start doing the really fun stuff!

Because strings are lists, that means we can iterate through a string using for or while loops. This opens up a whole
range of possibilities of ways we can manipulate and analyze strings. Let’s take a look at an example.
"""
def print_each_letter(word):
  for letter in word:
    print(letter)
"""
This code will iterate through each letter in a given word and will print it to the terminal.
"""
favorite_color = "blue"
print_each_letter(favorite_color)
# => 'b'
# => 'l'
# => 'u'
# => 'e'
"""
Let’s try a couple of problems where we need to iterate through a string.
Instructions
1.

Let’s replicate a function you are already familiar with, len().

Write a new function called get_length() that takes a string as an input and returns the number of characters in that
string. Do this by iterating through the string, don’t cheat and use len()!

Using a counter variable and a for loop is a great way to count things. For example look at the following code:
"""
counter = 0
for something in something_else:
  counter += 1
"""
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    Why don’t we have to initialize the variable of a for loop?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""

"""

Introduction to Strings
Strings and Conditionals (Part One)

Now that we are iterating through strings, we can really explore the potential of strings. When we iterate through a
string we do something with each character. By including conditional statements inside of these iterations, we can start
to do some really cool stuff.

Take a look at the following code:
"""
favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter)
"""
This code will count the number of bs in the string “blueberry” (hint: it’s two). Let’s take a moment and break down
what exactly this code is doing.

First, we define our string, favorite_fruit, and a variable called counter, which we set equal to zero. Then the for
loop will iterate through each character in favorite_fruit and compare it to the letter b.

Each time a character equals b the code will increase the variable counter by one. Then, once all characters have been
checked, the code will print the counter, telling us how many bs were in “blueberry”. This is a great example of how
iterating through a string can be used to solve a specific application, in this case counting a certain letter in a
word.
Instructions
1.

Write a function called letter_check that takes two inputs, word and letter.

This function should return True if the word contains the letter and False if it does not.

Make sure to print() the letter_check() function when testing it. To test try running:
"""
print(letter_check("strawberry", "a"))
"""
and
"""
print(letter_check("strawberry", "o"))
"""
What do you expect the function to return when you run these? What does it return?
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    Within a for loop, does every if statement need an else?

Why doesn’t else: return False work?
How does the indentation level of return False change the code?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""

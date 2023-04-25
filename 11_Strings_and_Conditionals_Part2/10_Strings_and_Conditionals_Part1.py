"""

Introduction to Strings
Strings and Conditionals (Part Two)

There’s an even easier way than iterating through the entire string to determine if a character is in a string. We can
do this type of check more efficiently using in. in checks if one string is part of another string.

Here is what the syntax of in looks like:
"""
letter in word
"""
Here, letter in word is a boolean expression that is True if the string letter is in the string word. Here are some
examples:
"""
print("e" in "blueberry")
# => True
print("a" in "blueberry")
# => False
"""
In fact, this method is more powerful than the function you wrote in the last exercise because it not only works with
letters, but with entire strings as well.
"""
print("blue" in "blueberry")
# => True
print("blue" in "strawberry")
# => False
"""
It can be helpful to include more than one boolean expression in the same line of code. To do this, use and or and not
in between the boolean expressions.
"""
print("e" in "blueberry" and "e" in "carrot")
# => False
print("e" in "blueberry" and not "e" in "carrot")
# => True
"""
The first example above is False because ONE of the expressions was False; there is no “e” in “carrot”. The second
example is True because there is an “e” in “blueberry” and not an “e” in “carrot”; both expressions are True.
Instructions
1.

Write a function called contains that takes two arguments, big_string and little_string and returns True if big_string
contains little_string.

For example contains("watermelon", "melon") should return True and contains("watermelon", "berry") should return False.
2.

Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with
all of the letters they have in common.

The letters in the returned list should be unique. For example,
"""
common_letters("banana", "cream")
"""
should return ['a'].

.append() will be useful in adding the shared letters to the list you will eventually return.

Also, make sure to test your function!
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    How to avoid duplicate letters?

I tried to brute force the solution, does this work?
Can the in operator be used to get the specific index of duplicate characters?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""

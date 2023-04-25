first_name = "Rodrigo"
last_name = "Villanueva"

"""
####################  theory  ########################

Introduction to Strings
Cut Me a Slice of String

Not only can we select a single character from a string, but we can also select entire chunks of characters from a
string. We can do this with the following syntax:

string[first_index:last_index]

This is called slicing a string. When we slice a string we are creating a substring - a brand new string that starts at
(and includes) the first_index and ends at (but excludes) the last_index.

Let’s look at some examples of this. Recall our favorite fruit:
"""
favorite_fruit = "blueberry"
"""
The indices of this string are shown in the diagram below.

Blueberry String

Let’s say we wanted a new string that contains the letters be. We could slice favorite_fruit as follows:
"""
print(favorite_fruit[4:6])
# Output: be
"""
Notice how the character at the first index, b, is included, but the character at the last index, r, is excluded. If you
look for the indices 4 and 6 in the diagram, you can see how the r is outside that range.

We can also have open-ended selections. If we remove the first index, the slice starts at the beginning of the string
and if we remove the second index the slice continues to the end of the string.
"""
print(favorite_fruit[:4])
# Output: blue

print (favorite_fruit[4:])
# Output: berry
"""
Again, notice how the b from berry is excluded from the first example and included in the second example.
Instructions
1.

You’re a programmer working for Copeland’s Corporate Company. At this company, each employee’s user name is generated by
taking the first five letters of their last name.

A new employee, Rodrigo Villanueva, is starting today and you need to create his account. His first_name and last_name
are stored as strings in script.py.

Create a variable new_account by slicing the first five letters of his last_name.

It should look something like:
"""
new_account = last_name[:5]
"""
2.

Temporary passwords for new employees are also generated from their last names.

Create a variable called temp_password by creating a slice out of the third through sixth letters of last_name. Your
string should have a total of 4 characters.

Remember, because indices start at 0, to get the third through sixth characters of a string you would want to use

string_name[2:6]

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    Can we only slice strings as a sequence of adjacent characters?

Still have questions? View this exercise's thread in the Codecademy Forums.



https://www.codecademy.com/resources/docs/python/substrings?page_ref=catalog
    Docs/    Python/    Substrings

Substrings

A substring is a sequence of characters that are part of an original string. In Python, substrings can be obtained by
using the slicing feature on a string variable. A slice can be made in a specific position within the string or it can
be made at the default index.
Syntax

A slice is made by using the open [ and closed ] square brackets next to a string variable. Inside the brackets, the
position can be given:

string[start:end:step]

    start defaults to 0 and gives the initial position the slice will start from.
    end defaults to -1 and is the position where the slicing will end.
    step defaults to 1 and indicates the number of steps to take in between indexes.

Examples

The following examples show different ways of obtaining substrings from an original string name.
"""
name = "Code Ninja"
"""
Retrieving Single Characters

When only one index is specified, a single character is returned. An index of 0 retrieves the first character of the string:
"""
print(name[0])

# Output: C
"""
Negative numbers work on the string backwards. For example, index -1 retrieves the last character of the string:
"""
print(name[-1])

# Output: a
"""
Negative Start Index

Using a negative start index (-n) with the default end value accesses the last n characters of the string. The following
gives access to the last three characters of the string:
"""
print(name[-3:])

# Output: nja
"""
End Index

To specify only an end index, use [:n], where n is the ending position. This will return the first n characters.
"""
print(name[:4])

# Output: Code
"""
Negative Step Value

Given a negative step value, returns the results backward:
"""
reversed = name[::-2]
print(reversed)

# Output: anNeo
"""
Keyword in

The in keyword can be used to check for a specific substring, like in the example below:
"""
print('de' in name)

# Output: True
"""
.find() Method

The string method .find() can also be used to find a subset. It returns the index of the first occurrence of the
substring. If the substring is not found, it returns -1.
"""
name = "Code Ninja"
print(name.find('ni'))
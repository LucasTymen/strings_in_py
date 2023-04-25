"""
Introduction to Strings
Negative Indices

In the previous exercise, we used len() to get a slice of characters at the end of a string.

There’s a much easier way to do this — we can use negative indices! Negative indices count backward from the end of the string, so string_name[-1] is the last character of the string, string_name[-2] is the second last character of the string, etc.

Here are some examples:
"""
favorite_fruit = 'blueberry'
print(favorite_fruit[-1])
# => 'y'

print(favorite_fruit[-2])
# => 'r'

print(favorite_fruit[-3:])
# => 'rry'
"""
Notice that we are able to slice the last three characters of ‘blueberry’ by having a starting index of -3 and omitting a final index.
Instructions
1.

Use negative indices to find the second to last character in company_motto. Save this to the variable second_to_last.
2.

Use negative indices to create a slice of the last 4 characters in company_motto. Save this to the variable final_word.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    What happens if we try to access an invalid index of a string?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""

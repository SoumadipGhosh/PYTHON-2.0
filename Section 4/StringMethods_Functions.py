# name="Harry" # string is immutable..

'''name[0]='j' # this will give an error because strings are immutable
'''
# a=len(name) # len() function gives the length of the string
# print(a)

# s="hello world" # string is immutable..
# print(s.upper() ,s) # converts string to upper case but the original string remains unchanged
# print(s.lower()) # converts string to lower case but the original string remains unchanged
# print(s.capitalize()) # capitalizes the first letter of the string but the original string remains unchanged
# print(s.title()) # capitalizes the first letter of each word in the string but the original string remains unchanged

# text = " hello world "
# print(text.strip()) # Output: "hello world" remove leading and trailing whitespace
# print(text.lstrip()) # Output: "hello world " remove leading / left whitespace
# print(text.rstrip()) # Output: " hello world" remove trailing / right whitespace

# text="Python is fun"
# print(text.find("is")) # Output: 7 find the index of the first occurrence of a substring
# print(text.replace("fun", "awesome")) # Output: "Python is awesome" replace a substring with another substring

# text="apples,bananas,cherries"

# print(text.split(","))  # Output: ['apples', 'bananas', 'cherries'] split the string into a list using a delimiter
# print(",".join(['apples', 'bananas', 'cherries']))  # Output: "apples,bananas,cherries" join a list of strings into a single string using a delimiter

text = "Python123"
print(text.isalpha()) # Output: False # checks if all characters are alphabetic
print(text.isdigit()) # Output: False # checks if all characters are digits
print(text.isalnum()) # Output: True # checks if all characters are alphanumeric (letters and digits)
print(text.isspace()) # Output: False # checks if all characters are whitespace
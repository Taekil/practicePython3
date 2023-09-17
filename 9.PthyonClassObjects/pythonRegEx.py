# RegEx: Regular Expression, 
# the sequence of charaters forming a search pattern. 

# RegEx can be used to check if a string contains the 
# specific search pattern. 

import re # bult-in re

txt = "The rain in Spain"
x = re.search("^The.*spain$", txt)

if x:
    print("YES")
else:
    print("NO")

# MetaCharacters
# https://www.w3schools.com/python/python_regex.asp

# [] a set of characters,  [a-m], find all lower characters alphabetically between
# "a" and "m"
# x = re.findall("[a-m]". txt) 

"""
# the search() function
# the search() function searches the string for a match, and
# returns a match object if there is a match. 
# if there is more than one match, only the first occurence of the
# match will be returned. 
"""
"""
the split() function
returns a list wereh the string has been split at each match. 

if no matches are found, the value non is reuturned.

you can control the number of occurence by specifying the maxsplit parameter. 

example. 
split the string only at the first occurence:
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
"""

"""
the sub() function
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

replace every white-space character with the number 9.

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
replace the first 2 occurences
"""
"""
Match Object
a match object is an object containing information about the search and the result. 

"""








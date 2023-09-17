"""

https://www.w3schools.com/python/python_file_open.asp

web application. 
creating, reading, updating, and deleting files. 

open(): filename and mode

"r" - read, defualt value, open a file for reading, error if 
the file does not exist

"a" - append, pend a file for appending, creates the file if it 
does not exist. 

"w" - write, open a file for writing, creates the file if it 
does not exist.

"x" - create, create the specified file, returns an error 
if the file exists. 

"t" - Text -> text mode
"b" binary mode (e.g. images)

"""

f = open("demofile.txt")
# the code above is the same as:
f = open("demofile.txt", "rt")
# because "r" for read and "t" for text are the default values

"""
open a file on the server
assume we have the following file, located in the same 
folder as python

demofile.txt
"""
# the open() function returns a file object, which has a read() 
# method for reading the content of the file
f = open("demofile.txt", "r")
print(f.read())

# if the file is located in a diffrent location, you will 
# have to specify the file path, like this:
f = open("D:\\myfiles\welcome.txt". "r")
print(f.read())

# read only part of the file
print(f.read(5)) # we can also specify how many characters we want to return. 

# read lines
print(f.readline())

# by calling readline() two times, you can read the two first lines, 
print(f.readline())
print(f.readline())

# by looping through the lines of the file, you can read the whole file, 
# line by line

f = open("demo.txt", "r")
for x in f:
    print(x)

# close files
# it is good practice to always close the file when you are done with it

f.close()

"""
Python file write
write to an existing file
to write to an existing file, you must add a parameter to the open() function. 
"a" append - append to the end of the file
"w" write - overwrite any existing content
"""

f = open("demofil2.txt", "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending
f = open("demofile2.txt", "r")
print(f.read())

# open the file "demofile3.txt" and overwrite the content
f = open("demofile3.txt", "w")
f.write("woop! I have deleted the content")
f.close()

# open and read the file after the overwriting
f = open("demofile3.txt", "r")
print(f.read())

"""
create a new file

"x" create
"a" append
"w" write
"""

f = open("myfile.txt", "x")

# create a new file if it does not exist
f = open("myfile.txt", "w")

"""
python delete file

os.remove() function, to delete a file, we must import the OS module(why?)

import os
os.remove("demofile.txt")

check if file exist, 
to avoid getting an error, you might want to check if the file exists
before you try to delete it

example
check if file exists, then delete it

import os
if os.path.exists("demofile.txt")
    os.remove("demofile.txt")
else:
    print("the file does not exist")

delete folder
remove the folder "myfolder"

import os
os.rmdir("myfolder")
"""





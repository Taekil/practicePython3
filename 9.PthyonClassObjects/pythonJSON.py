# what is JSON?
# a syntax for storing and exchanging data. 
# built-in package called json. 
import json
# some json
x = '{"name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a python dictionary
print(y["age"])

# covert from python to JSON
# a python object (dict):
x = {
    "name" : "John",
    "age" : 30,
    "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

# convert python objs of the following types, 
# into JSON strings

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "Divorced": False,
    "Children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {
            "model":"BMW 230", "mpg":27.5
        },
        {
            "model":"Ford Edge", "mpg":24.1
        }
    ]
}
y = json.dumps(x)
print(y)

# format the result
# use the indent parameter to define the numbers of indents
# what is indents?
json.dumps(y, indent = 4)

json.dumps(y, indent = 4, separators=(". ", " = "))

json.dumps(y, indent = 4, sort_keys= True)





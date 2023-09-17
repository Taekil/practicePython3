# https://www.w3schools.com/python/python_tuples_access.asp

# access tuple items
# index number
thisTuples = ("apple", "banana", "cherry")
print("thisTuples[1]", thisTuples[1])

# negative indexing
# -1 is the last item
# -2 is the second last item
print("thisTuples[-1]", thisTuples[-1])
print("thisTuples[-2]", thisTuples[-2])

# range of indexing
thisTuples = ("apple", "banana", "cherry", "orange", "kiwi", 
              "melon", "mango")
print("thisTuples[2:5]", thisTuples[2:5])
print("thisTuples[:4]", thisTuples[:4])
print("thisTuples[2:]", thisTuples[2:])
print("thisTuples[-4:-1]", thisTuples[-4:-1])
if "apple" in thisTuples:
    print("YES, 'apple' is in the fruitTuple")


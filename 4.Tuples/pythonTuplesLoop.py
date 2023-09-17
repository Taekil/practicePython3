# loop through a tuple
# https://www.w3schools.com/python/python_tuples_loop.asp

thisTuple = ("apple", "banana", "cherry")
for x in thisTuple:
    print(x)

for i in range(len(thisTuple)):
    print(thisTuple[i])

i = 0
while i < len(thisTuple):
    print(thisTuple[i])
    i += 1

# join tuples
# https://www.w3schools.com/python/python_tuples_loop.asp
tuple1  = ("a", "b", "C")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(f"tuple3: {tuple3}")
multiple = tuple1 * 2
print(f"multiple: {multiple}")


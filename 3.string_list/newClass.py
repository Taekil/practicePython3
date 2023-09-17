from random import choice
# object class

class Square:
	def __init__(self, val):
		self.val = val
	def getVal(self):
		return self.val*self.val

class fruit:
	def __init__(self):
		self.fruitList = ["apple", "Pear", "Banana"]
	def getFruit(self):
		return print(choice(self.fruitList))


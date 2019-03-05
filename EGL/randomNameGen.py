from random import randint
print ("Hello World")
# print (randint(0,100))  # exception that is higher range is included

def createRandomName(x):
	alpha="abcde" # Sample Space for picking up random characters
	temp="" # For  Concat operation ahead
	for y in range(x):
		temp+=alpha[randint(0,len(alpha)-1)]
	return temp


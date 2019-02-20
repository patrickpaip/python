from random import randint

def getMeName(s):
	alpha="abcde"
	temp=""
	for x in range(s):
		temp+=alpha[randint(0,len(alpha)-1)]
	return temp

def hello():
	print ("Something")

# Scopes
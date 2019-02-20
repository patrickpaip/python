# def backup():
# 	print ("Backup")

# def erase():
# 	print ("Erase")

# def printer():
# 	print ("Printer")

# def backup1():
# 	print ("Backup1")

# def erase1():
# 	print ("Erase1")

# def printer1():
# 	print ("Printer1")

# repo=[backup,erase,printer,backup1,erase1,printer1] # All Commands
# command=["1001","1003","1004","1010"]  # Command from Server [Assume]
# mapper_dict={"1001":backup,"1002":erase,"1003":printer,"1004":backup1}
# print (mapper_dict)
# mapper_dict["1010"]=repo[-1]  # adding dynamically 
# print (mapper_dict)
# for x in command:
# 	if(x in mapper_dict): # Checking if key is available
# 		mapper_dict[x]()   # Call the value since its a function address
# 	else:
# 		print ("Invalid Command",x)

# dict_b={"name":"batman"}
# def pop1(key,default):
# 	if(key in dict_b):
# 		value=dict_b[key]
# 		del dict_b[key]
# 		return value
# 	else:
# 		return default

# # Call in sequence
# mapper_list=[backup,erase,printer,backup1,erase1,printer1]
# for x in mapper_list:
# 	x()

# # mapping of functions to Arrays
# command=[0,3,5]  # Assume someone has sent this command which contains indexes
# mapper_list=[backup,erase,printer,backup1,erase1,printer1] # Store Address of Functions
# for x in command:
# 	mapper_list[x]()   # Call the respective addresses

# # Q
# mapper_list=[backup(),erase(),printer(),backup1(),erase1(),printer1()]
# print (mapper_list)

# def F1(a,b):
# 	print (a,b)

# F1(1,2)

# # Program to Accept multiple unnamed arguments
# def F2(*args):  # * signifies that it can accept many parameters
# 	print (args) # While using it, use only the variable name without *
# 	for x in args: # its a tuple, thus iterable
# 		print (x)

# F2(1,2) # No or any number of parameter is accepetable

# def printme(*args):
# 	temp=""
# 	for x in args: 
# 		temp+=str(x)+":"
# 	print (temp[:-1])

# printme(1,2,3,"hello")
# Receiving Named Parameters
# def printme1(**kwargs):
# 	print (kwargs)
# 	print (kwargs["name"])
# # Function Call	
# printme1(name="batman",age=24)

# def printme2(a,*args,b=3,**kwargs):
# 	print(a)
# 	print (b)
# 	print (args)
# 	print (kwargs)

# printme2(1,2,3,4,5,6,7,name="batman",b=7)

# dict_a={"name":"batman","age":40,"place":"gotham"}
# print (dict_a["name"])
# print (dict_a["place"])
# print (dict_a["age"])
# print (dict_a)
# # print (dict_a["country"]) # KeyError
# if ("country" in dict_a): # Compares only the keys
# 	print (dict_a["country"])
# else:
# 	print ("No country")

# print (dict_a.keys()) #
# print (dict_a.values())

# for x,y in dict_a.items():
# 	print ("%s:%s"%(x,y))

# # Editables
# dict_a["place"]="Bangalore"  # Key is Present
# dict_a["vehicle"]="batmobil"  # Key is Absent
# print (dict_a)
# # Removal
# a=dict_a.pop("country",None)
# print (a)
# print (dict_a)
# # del dict_a["country"]


from random import randint
a=randint(0,100)
b=randint(0,50)

# Problem Statement
# 1) Create a function which generates 6 lettered random word
#    from the namespace a-z (Strictly No use of inbuilt function)
# Output1:
# [[23,45],[56,67],[89,56]...100]
# Output2: 
# [["dsadas",34],["gdfggh",56]....100]
# Extension of output1: get the avg of 2 entities in a seperate list
# Extension of output2: create a list of dictionary , with keys name and age

# [[23,45],[56,67],[89,56]...100]

# from random import randint

# def getMeName(s):
# 	alpha="abcde"
# 	temp=""
# 	for x in range(s):
# 		temp+=alpha[randint(0,len(alpha)-1)]
# 	return temp

# list_a=[]
# list_avg=[]
# for x in range(100):
# 	a=randint(0,100)
# 	b=randint(0,100)
# 	list_a.append([a,b])
# 	list_avg.append((a+b)/2)
# print ("LIST:",list_a)
# print ("AVG:",list_avg)

# list_c=[]
# for x in range(100):
# 	b=randint(0,100)
# 	list_c.append([getMeName(6),b])
# print ("LISTC:",list_c)











#Dictionary
# Key -> Value
# Rules
# Functions






# Scopes
# Parameters
# Lambda





# import json
# a={
# 	"name": "Batman",
# 	"pass" : None,
# 	"mobile": "9845098450",
# 	"active" : False,
# 	"address" : [{
# 	   "type" : "home",
# 	   "pincode" : "00001"
# 	},
# 	{
# 	   "type" : "office",
# 	   "pincode" : "00002"
# 	}]
# }
# print (a)
# print (type(a))
# data=json.dumps(a)   # Format to String
# print (data)
# print (type(data))
# data1=json.loads(data)  # String to Format
# print (data1)
# print (type(data1))

# # print (a["address"])
# # print (len(a["address"]))
# # print (a["address"][-1]["pincode"])
# # for x in a["address"]:
# # 	print ("type:",x["type"],"pincode:",x["pincode"])

# <xml>	
# 	<msg>
# 		<title>A</title>
# 		<seen>true</seen>
# 		<time>15232335</time>
# 	</msg>
#    <msg>
# 		<title>A</title>
# 		<seen>true</seen>
# 		<time>15232335</time>
# 	</msg>
# </xml>

# [
# 	{
# 		"title" : "A",
# 		"seen" : true
# 	},

# 	{
# 		"title" : "A",
# 		"seen" : true,
# 		"time" : 152323232
# 	}
# ]

# [
#  ["title","seen","time"],
#  ["A",true,15343443],
#  ["A",true,15343443]
# ]


# import json
# # import pickle
# # import bson
# dict_a={"name":"batman","age":50}
# print (dict_a)
# data=json.dumps(dict_a,indent=4)
# print (data)

a=4
def F1():
	a=5
	def F2():
		nonlocal a
		a=6
		print ("INSIDE F2",a)
	F2()
	print ("INSIDE F1",a)

F1()

# print ("OUTER LEVEL:",a)

def F3():
	def F4():
		print ("F4")
	return F4

a=F3()
b=F3()
print (type(a))
print (a)
print (b)
print (F3)
print (F3)











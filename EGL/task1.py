'''
a=4
a=a**3  # Raising the power by 2
print (a)
'''
# Points to Note:
# Indexes are integers
# Indexes Starts from 0

# a="Hello World"
# print (len(a))   # To Find Length of a string len()
# print (a[0])
# print (a[4])
# print (a[-1])  # result len() is one greater than the last index
# Splicing

# Range: Lower Range is included
# 	   Higher Range is not included
# print (a[0:5])  # Hello
# print (a[6:11])
# print (a[:5])
# print (a[6:])
# print (a[:])   # Cloning
# print (a[::2]) # Result?
# # Lower Range Delimiter High range Delimiter Increment
# print (a[::-1])

# a="Hello"
# b=" World"
# c=a+b
# c='F'+a[1:]+' F'+b[2:]
# print (c) #Fello Forl

# b="Hello"
# c=b[:]  # c will have address of b, it will point to the same hel
# Example Cloning
# a=4
# print (a==4)
# print (a is 4)   # Do not use it  ' is Operator'
# print (a!=4)
# print (a is not 4)  # Do not use it
# print (a>4)
# print (a>=4) # Greater than Equal to
# a=4
# b=5
# print (a>3 and b>5)
# print (a>3 or b>5)
# a=True

# print (not a)

# a=4
# if(a is 4):
# 	print ("Its 4")
# elif (a==5):
# 	print ("its 5")
# elif (a is not 6): 
# 	print ("its 6")
# elif (a is 7):
# 	print ("its 7")
# else:
# 	print ("Something else")

# Checking if something is inside a variable
# f="Hello World"
# if ('e' in f):
# 	print ("E Exist")
# else:
# 	print ('E is not present')

# if ('Fello' not in f):
# 	print ("Fello Doesnt Exist")
# else:
# 	print ('Exists')

# if the string contains '#' then print the reversed string
# else just print the string
# inputVar="Hello World#"
# if('#' in inputVar):
# 	print (inputVar[::-1])  # Reversing the String
# else:
# 	print (inputVar)

# a="One"
# b=6
# c=a+str(b)
# print (c)

# counter=0
# while(counter<100):
# 	print (counter)
# 	counter=counter+1
# 	# counter+=1 # ShortHand Operators

# a="I am learning Python"
# l=len(a)  # Getting the Length of the string
# counter=0  # Initial Number
# print ("-----------Printing Started----------")
# while(counter<l):  # Iterates Until Condition is False
# 	if(a[counter]!=" "):  # Checking if the current value is space
# 		print (a[counter])   # Picks the data using Index of String
# 	counter+=1  # Note: ++ operator isnt there in Python
# print ("-----------Printing Done--------------")

# # Print all even numbers between 100 to 200
# counter=100
# while(counter<200):
# 	if(counter%2==0):
# 		print (counter)
# 	counter+=1

# For loop in Python!
# a="Hello World"
# for x in a:
# 	print (x)

# # n times
# for x in range(0,100):
# 	print (x)

# for x,y in enumerate(a):  # x as an index and y as value
# 	print (x,y)

# When you are splicing -> new list
# print (list_a)  # print the whole list
# print (list_a[-1]) # has Negative Indexes
# print (list_a[:3]) # Splicing gives back
# print (list_a[::2]) # Skip every one item and print
# list_a[0]=99  # Item Assignment is allowed
# print (list_a)

# for x in list_a:
# 	print (x)

# for x,y in enumerate(list_a):
# 	print (x,y)










# for <TempVar> in <Iterator>:
# 	print (<TempVar>)



# # The original List gets manipulated
# list_a=[1,2,3,"Hello",True]
# list_a.append("Okay")  # Add to the End of the list
# print (list_a)
# list_a.insert(len(list_a),"World")  # Append Using Insert
# print (list_a)
# list_a.remove("Hello") # Remove by Value
# print (list_a)
# del list_a[0]   # Delete by Index

# list_a=[1,2]
# list_b=[3,4]
# list_c=list_a+list_b   # Adding ListA and B to produce a new list C
# print (list_c)
# list_a.extend(list_b)  # Editing ListA
# print (list_a)

# list_a=[1,2]
# list_b=[3,4]
# # Shallow Copy
# # list_a.append(list(list_b)) # Cloned its name is not list_b
# list_a.append(list_b.copy())
# # list_a.append(list_b[:])
# list_b[0]=99
# print (list_b)
# print (list_a)

# list_b=[#105,#104]
# list_a=[#100,#101,#102]
# list_b[0]=99
###############

### [1,2,4, listC]

######LEVEL1##### 1 2 3 list_b


# import copy
# a=[1,2]
# b=[3,4]
# c=[5,6]
# b.append(c)
# print (b)
# a.append(copy.deepcopy(b))
# print (a)
# b[0]=99
# c[-1]=999
# print (a)
# Higher order Functions

# Use Case
# list_a=[1,2]
# print (list_a.append("Hello"))

# x=4
# y=6
# print (x,y)
# a=y,x,1,2,3,4
# for x in a:
# 	print (x)

# a="Hello World"
# for x,y in enumerate(a):
# 	print (x,y)

# for x in enumerate(a):
# 	print (x[0],x[1])

# Tuples are non editable version of list
# Tuples can be spliced
# A comma at the end of the tuple is a good practice
# Multiple return types are nothing but tuples
# tuple_a=(1,2,3,4,5,6,7,8,)
# print (id(tuple_a))
# f=tuple_a[:4:2]
# print (id(f))
# print (f)
# How do you find a value is inside a tuple?
# say value is 5
# In Operator has to be used. Think English!!
# if(5 in tuple_a):
# 	print ("its 5")
# Enumeration is also possible for tuple just like list/strings
# for x,y in enumerate(tuple_a):
# 	print (x,y)

# Function Arguments
### Without Arguments
# def clickme1():
# 	print ("Hello World")
# clickme1()
### Positional Arguments
# def clickme2(a,b):
# 	print (a,b)
# clickme2(2,5)
############## Default Arguments
# The Minimum no of parameter to be sent 
# is 1 since b has a default value
# def clickme3(a,b=4):
# 	print (a,b)
# clickme3(2)

# Example
# Format needs to be sent only when its other format
# Else
# def clickme2(data,format="utf-8"):
# 	print (data,format)
# clickme2("Hello World")
# clickme2("Hello World","utf-7")
# Check all Combinations
# def connectftp(username,password,secure=False,port=21):
# 	print (username,password,secure,port)
# connectftp("root","secret",port="22",secure=True)
######## MULTIPLE ARGUMENTS #############
# While Accessing the args, do not use *
# def clickme4(*args):
# 	print (args)
# 	for x in args:
# 		print (x)
# clickme4(1,2,3,4,5,6,7,8)

# # if default argument i.e. b=6 is placed before *args, then it
# # will get assigned automatically
# def clickme5(a,b=6,*args):
# 	print (a)
# 	print (b)
# 	print (args)
# clickme5(1,2,3,4,5)
# # But if placed after args, then explicit key value pair
# # has to be provided
# def clickme6(a,*args,b=6):
# 	print (a)
# 	print (b)
# 	print (args)
# clickme6(1,2,3,4,"hello",b=10)

# def clickme7(**kwargs):
# 	print (kwargs)

# clickme7(b=4,c=40)

# def clickme8(a,b,*args,name="batman",**kwargs):
# 	print ('a',a)
# 	print ('b',b)
# 	print ('args',args)
# 	print ('name',name)
# 	print ('kwargs',kwargs)
# clickme8(1,2,3,434,343,indent=4,connection="secure",name="superman")



# dict_a={}  # Mutable Types # Empty Declaration is also possible
# dict_a={'name':'fidelity','place':'egl'}  # single quote and double quotes, both acceptable
# print(dict_a)
# # if a key is present, then the value would be returned
# # if key not present, then keyError would be raised
# print (dict_a['name'])
# # If a key is not present, and if you are
# # assigning value to a key, the the key value
# # pair would be added to the dictionary
# dict_a['altitude']=90  # Value can be anything
# # if the key is present, and you are assigning value
# # then the old value gets replaced by the new one
# dict_a['altitude']=180
# print(dict_a)
# # try deleting an index
# # if the index is not present, it would raise error
# del dict_a["altitude"] # Del command is universal
# # if key is present, you get the value,
# # else you would get the default return placed at the
# # 2nd parameter (its optional)
# # Pop Operation returns the value and deletes from
# # the dictionary
# value=dict_a.pop('place',None)
# print ('value of pop',value)
# # Checking if a key is present inside the dictionary 
# # using in operator
# if ("altitude" in dict_a):
# 	print ("name exist",dict_a["name"])
# else:
# 	print ("It Doesnt Exist")
# # Iterating using forloop
# # When you are iterating using forloop, only key will
# # be taken as data not the value
# for x in dict_a:
# 	print (x)
# # To get both key and the value, .items() has be used instead
# # of enumerate
# for x,y in dict_a.items():
# 	print (x,y)
# # Get all the keys
# print (dict_a.keys())
# # Get all the values
# print (dict_a.values())
# ##### print all the values one by one
# #??? Which of the following is better?
# #AAAAA
# for x in dict_a.values():   # Inefficient
# 	print (x)
# #BBBBB
# for x,y in dict_a.items():  # efficient, since it uses lazy evaluation
# 	print (y)

# # Input Source
# command = ["1009","1003","1002"] 
# def backup():
# 	print ("backup")
# def printer():
# 	print ("Printer")
# def logger():
# 	print ("Logger")
# def shutdown():
# 	print ("Shutting Down")

# mapper={
# 	'1001' : backup,
# 	'1002' : printer,
# 	'1003' : logger,
# 	'1004' : shutdown
# }
# for x in command:
# 	if (x in mapper):
# 		mapper[x]()
# 	else:
# 		print ("Command not Found",x)


# Formatting of this is called JSON
# A combination of list and dictionaries
# a list
# a list of list
# a dictionary
# a dictionary with an value as list

# print (a[0])
# print ('batman has',len(a[0]["address"]),"addresses")
# print (a[0]["address"][0])
# print (a[0]["address"][-1]["pincode"])

##############################################################
#####################JSON CONVERSION##########################
##############################################################

# import json # Library to load and unload JSON formats/Strings
# a={ 'key1': None, 'key2' : True, 'key3' : 'Batman'} # Python
# # a=[1,2,3,4,5,True,None,"hello"] # a list is also accepted
# print (a)
# print (type(a)) # Type is Dict
# data=json.dumps(a)    # JSON Format to JSON String
# # data=json.dumps(a,indent=4) # Adds indentation
# # and is used only for human readable files, not for transmission. 
# print (data)
# print (type(data))   # Type will be strings
# data1=json.loads(data) # JSON String to JSON Format
# print (data1)  
# print (type(data1))  # Type will be Dict
# # Ways to identify whether its a string or format
# # use Type() or the output will have "" if its a string.

##########################################################
#######################MODULES############################
# Seperating your code logic into multiple files

# import randomNameGen  # import complete file contents
# print (randomNameGen)
# print (randomNameGen.createRandomName(6))
# print (randomNameGen.createRandomName)

# from randomNameGen import createRandomName    # selective Importing
# print (createRandomName(6))
# import randomNameGen as ran   # Alias
# print (ran.createRandomName(6))

# Read
# if the file does not exist, raises an error -> FileNotFoundError
# file=open("sample.txt","r")
# data=file.read()  # reads the complete file at once and keeps the
# #file pointer at the end
# # data2=file.read() # This would be empty
# print (data)
# file.close()  # limit is 2 power 16
# # # Write
# file=open("sampleoutcome","w")
# file.write("Just Wrote")
# file.close()
# # # Append
# file=open("samplelog","a")
# file.write("Oops\n")
# file.close()

# #######################BREAK!!!!!#####################

# Benefits of Context Manager
# Auto Close of Files
# import json
# # Read an JSON using context manager
# with open("sample.json") as file:
# 	data=file.read()  # read the complete File
# 	print (json.loads(data))  # convert from JSON string to Format

# # Write an JSON using context manager
# with open("outcome1.json","w") as file:
# 	a={'name':'value'} # Sample data to be written
# 	file.write(json.dumps(a,indent=4))  # Convert JSON format to String


# How to read a JSON File
# How to Write as a JSON File
# How to Read using Delimiters
# Concept of Exception Handling
# Things to take care
# Comprehensions
# Links

############ READ AND WRITE TO ANOTHER FILE##########
# # open the File
# file=open("sample.txt","r")
# # Read the File content and store to temp variable data
# data=file.read()
# # Open another file in write Mode
# file1=open("newfile.txt","w")
# # Write the Content of previous file to the new file
# file1.write(data)
# # Close the file1
# file1.close()
# # Close the original file
# file.close()
# ###################################################4
# # Using Context manager making a duplicate
# with open("sample.txt","r") as file:
# 	with open("newfile1.txt","w") as file1:
# 		file1.write(file.read())
# import json
# with open("package.json","r") as file:
# 	data=json.loads(file.read())
# 	if("license" in data):
# 		print ("Proceed")
# 		if(data["license"]=="ABCD"):
# 			print ("Start Software")
# 			f={
# 				'name' : 'me',
# 				'age' : 100
# 			}
# 			with open("outcome.json","w") as file1:
# 				file1.write(json.dumps(f))
# 		else:
# 			print ("Invalid License")
# 	else:
# 		print ("License doesnt exist")

# with open("outcome.json") as file:
# 	data=json.loads(file.read())
# 	print (data['name'])

# import time
# while(True):
# 	file=open("command.json","r")
# 	command=json.loads(file.read())
# 	file.close()


# 	def backup():
# 		print ("backup")
# 	def printer():
# 		print ("Printer")
# 	def logger():
# 		print ("Logger")
# 	def shutdown():
# 		print ("Shutting Down")

# 	mapper={
# 		'1001' : backup,
# 		'1002' : printer,
# 		'1003' : logger,
# 		'1004' : shutdown
# 	}
# 	for x in command:
# 		if (x in mapper):
# 			mapper[x]()
# 		else:
# 			print ("Command not Found",x)
# 	time.sleep(10)

#Input Source
try:
	a={}
	# print (a['name'])
	# print (1/0)
	file=open("samplexy.json","r") # Vulnerable Code
	# try:
	# 	data=file.write()
	# except:
	# 	print ("Some reading issue")
	# finally:
	# 	file.close()
except (FileNotFoundError,NameError):
	print ("Some Issue F1")
except KeyError:
	print ('Key Error found')
except:
	print ("Some Issue F3")





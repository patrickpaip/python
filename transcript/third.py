# # Read Mode
# file=open("sample.txt","r")   # For ReadOnly, File has to exist
# data=file.read()  #Reading the whole file at once
# print (data)
# file.close()   # mandatory Step
# # Write Mode
# file=open("sample1.txt","w")  # File would be created if it doesnt exist
# file.write("Hello World")   # File gets truncated and over written
# file.close() 
# # Append Mode
# file=open("sample2.txt","a")  
# file.write("hello World\n")
# file.close()


'''
Create a json file named "settings.json" with the following conditions
1) "license" An alphanumeric licence key
2) "username" An user defined username, minimum 6 characters
3) "time" Time in terms of epoch time (Integer Check)
4) "id" An ID ranging between 0 to 100

Operations:
1) Check if all the attributes are available in the file
2) Validate the values
3) if "id" range is between 0 to 50, append "-add" to the
   username if not appended already
4) if Operation had any changes to the settings.json file,
   then write back to the same file, with a operation.log file
   containing username and time of operation
'''
# import json
# file=open("settings.json","r")
# data=json.loads(file.read())
# file.close()

# def logger(content):
# 	with open("operation.logs","a") as file:
# 		file.write(str(content)+"\n")

# def checkAttr(curData,list_x):
# 	for x in list_x:
# 		if(x not in curData):
# 			logger("Issue with Attributes Identification:"+x)
# 			return False
# 	return True

# def validate():
# 	if(not data["license"].isalnum()):
# 		logger("Validation Failure for license")
# 		return False
# 	elif(len(data["username"])<6):
# 		logger("Validation Failure for username")
# 		return False
# 	elif(not isinstance(data["time"],int)):
# 		logger("Validation Failure for time")
# 		return False
# 	elif(not 0<data["id"]<100):
# 		logger("Validation Failure for id")
# 		return False
# 	return True
# if(checkAttr(data,["license","username","time","id"])):
# 	print ("All attributes available")
# 	if(validate()):
# 		print ("Validation Success")
# 		if(0<data["id"]<50 and "-add" not in data["username"]):
# 			data["username"]+="-add"
# 			with open("settings.json","w") as file:
# 				file.write(json.dumps(data,indent=4))
# 			logger("settings.json updated")
# 		else:
# 			logger("Contraint Failed for Edit")

# 	else:
# 		print ("Validation Failure")
# else:
# 	print ("Oops")


'''
Question:
Create a file named "Hosts" without any extension
The Structure of the file is as follows
----------Contents----------
www.facebook.com 192.168.1.1
www.google.com 192.168.1.2
----------------------------
Convert the file to the following 3 JSON Pretty formats 
---------output1.json-------------
[
	{
		"url" : "www.facebook.com",
		"ip"  : "192.168.1.1" 
	},
	{
		"url" : "www.google.com",
		"ip"  : "192.168.1.2" 
	}
]
---------output2.json---------------
[
	["url","ip"],
	["www.facebook.com","192.168.1.1"],
	["www.google.com","192.168.1.2"]
]
--------output3.json----------------
{
	"www.facebook.com" : "192.168.1.1",
	"www.google.com"   : "192.168.1.2"
}
-------------------------------------
SYNTAXS Introduced or which can be used:
---->
file=open("filename")
for x in file:
	print (x)
---->
file=open("filename")
data=file.readlines()
---->
str.split or str.partition
'''

# with open("test.txt","r") as file:
# 	for x in file:
# 		print (x)

# with open("test.txt","r") as file:
# 	print (file.readlines())

# a="Hello,World,Good"
# b=a.split(",")
# print (b)
# c=a.partition(",")
# print (c)

# import json
# list_a=[]
# with open("test.txt","r") as f: # using context manager
# 	for x in f:  # read line by line, each line into x
# 		b=x.split()  # outcome is a list
# 		list_a.append(b)  # list inside a list

# def output1():
# 	list_temp=[]
# 	for x,y in list_a:
# 		list_temp.append({"url":x,"ip":y})
# 	with open("output1.json","w") as file:
# 		file.write(json.dumps(list_temp,indent=4))

# def output2():
# 	list_temp=list(list_a)
# 	list_temp.insert(0,["url","ip"])
# 	with open("output2.json","w") as file:
# 		file.write(json.dumps(list_temp,indent=4))

# def output3():
# 	dict_a={}
# 	for x,y in list_a:
# 		dict_a[x]=y
# 	with open("output3.json","w") as file:
# 		file.write(json.dumps(dict_a,indent=4))

# output1()
# output2()
# output3()


# import json
# from flask import Flask
# app = Flask(__name__)
# myval=""

# @app.route("/") # Decorator
# def hello():
# 	dict_a={"name":myval}
# 	return json.dumps(dict_a,indent=4)

# @app.route("/putdata/<content>") # Decorator
# def hello1(content):
# 	global myval
# 	myval=content
# 	return "Edited"

# if __name__ == '__main__':
# 	app.run("localhost",5000)


# http://localhost:5000



# Utilizing Sleep
# from time import time,sleep
# curTime1=time() 0
# curTime2=time() 0
# while(True):
# 	exacttime=time() 2
# 	if(exacttime-curTime1>=3):
# 		print ("OK")
# 		curTime1=exacttime
# 	if(exacttime-curTime2>=5):
# 		print ("NOT OK")
# 		curTime2=exacttime
# 	sleep(0.1)  # Very Important 

# from time import sleep
# from threading import Thread
# from multiprocessing import Queue

# inQ=Queue()

# def producer1():
# 	while(True):
# 		data=input("Enter Here")
# 		inQ.put(data)

# def consumer1():
# 	while(True):
# 		print ("Con1",inQ.get())


# t1=Thread(target=producer1)
# t1.start()
# t3=Thread(target=consumer1)
# t3.start()


# pymotw.com


# import sqlite3
# conn = sqlite3.connect('example.db')
# c = conn.cursor()
# # c.execute('''CREATE TABLE stocks
# #              (date text, trans text, symbol text, qty real, price real)''')

# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# # Save (commit) the changes
# conn.commit()

# for row in c.execute('SELECT * FROM stocks ORDER BY price'):
#         print(row)

# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# conn.close()

# import paho.mqtt.client as mqtt

# # The callback for when the client receives a CONNACK response from the server.
# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))

#     # Subscribing in on_connect() means that if we lose the connection and
#     # reconnect then subscriptions will be renewed.
#     client.subscribe("batmanpune")

# # The callback for when a PUBLISH message is received from the server.
# def on_message(client, userdata, msg):
#     print(msg.topic+" "+str(msg.payload))
#     client.
#     ("puneworld","Hey I am Alive",0,0)

# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message

# client.connect("broker.mqttdashboard.com", 1883, 60)

# # Blocking call that processes network traffic, dispatches callbacks and
# # handles reconnecting.
# # Other loop*() functions are available that give a threaded interface and a
# # manual interface.
# client.loop_forever()

try:
	file=open("HelloWorld.txt","r")
	print ("OK")
except (FileNotFoundError,NameError):
	print ("File not Found")
except KeyError:
	print ("File not Found")
except Exception as e:
	print ("File not Found",e)
else:
	print ("Else")
finally:
	print ("All the time")




try:
	file=open("host.txt")
	try:
		print (file.read())
	except:
		pass
	finally:
		file.close()
except:
	pass
finally:
	pass

pymotw.com

prathik@logichive.in
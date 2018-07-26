'''
Create a json file named "settings.json" with the following conditions
1) "license" An alphanumeric licence key
2) "username" An user defined username, minimum 6 characters
3) "time" Time in terms of epoch time
4) "id" An ID ranging between 0 to 100

Operations:
1) Check if all the attributes are available in the file
2) Validate the values
3) if "id" range is between 0 to 50, append "-add" to the
   username if not appeneded already
4) if Operation had any changes to the settings.json file,
   then write back to the same file, with a operation.log file
   containing username and time of operation
'''

import json
import time
# Read the File operation
file=open("settings.json")
data=file.read()
file.close()
op_content=json.loads(data)
if("license" in op_content and "username" in op_content and "time" in op_content and "id" in op_content):
	if(op_content["license"].isalnum() and len(op_content["username"])>=6 and op_content["id"]<100 and op_content["id"]>0):
		if( 0<op_content["id"]<50 and "-add" not in op_content["username"]):
			op_content["username"]+="-add"
			with open("settings.json","w") as file:
				file.write(json.dumps(op_content))
			with open("operation.log","a") as file:
				content="change: "+op_content["username"]+" at "+str(time.time())
				file.write(content+"\n")
		else:
			with open("operation.log","a") as file:
				content="No change: at "+str(time.time())
				file.write(content+"\n")
else:
	print ("Format Issue, Check Json File")

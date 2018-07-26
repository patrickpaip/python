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

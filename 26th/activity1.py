import json
# Read the File operation
file=open("settings.json")
data=file.read()
file.close()
op_content=json.loads(data)
if("license" in op_content and "username" in op_content and "time" in op_content and "id" in op_content):
	if(op_content["license"].isalnum() and len(op_content["username"])>=6 and op_content["id"]<100 and op_content["id"]>0):
		print ("Data Validated")
else:
	print ("Format Issue, Check Json File")
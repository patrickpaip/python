import json
file=open("inputs/hosts")
temp_list=[]
for x in file:
	temp_list.append(x.split())
file.close()
# Writing Output1.JSON
with open("outputs/output1.json","w") as file:
	list_a=[]
	for x in temp_list:
		list_a.append({"url":x[0],"ip":x[1]})
	file.write(json.dumps(list_a,indent=4))
	del list_a
# Writing Output2.JSON
with open("outputs/output2.json","w") as file:
	t_list=list(temp_list)
	t_list.insert(0,["url","ip"])
	file.write(json.dumps(t_list,indent=4))
	del t_list
# Writing Output3.JSON
with open("outputs/output3.json","w") as file:
	dict_a={}
	for x in temp_list:
		dict_a[x[0]]=x[1]
	file.write(json.dumps(dict_a,indent=4))
	del dict_a
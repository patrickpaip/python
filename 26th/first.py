
file=open("input.txt","r")
print (file.read())
file.close()

file=open("input.txt","w")
file.write("Im Good, Very Good")
file.close()

with open("input.txt","w") as file:
	print (file.write("OK"))

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


http://collabedit.com/r5b7m









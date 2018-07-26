from flask import Flask,request
from multiprocessing import Queue
import threading
import time
import json

app = Flask(__name__)
inQ=Queue()


def erase(*args):
	print ("Erasing Started")
	time.sleep(3)
	print ("Erased")

def backup(*args):
	print ("Backup Started")
	time.sleep(2)
	print ("Backup:",args)


@app.route("/command",methods=["POST"])
def getdatapost():
	if("comm" in request.form):
		inQ.put({"comm":request.form["comm"],"data":request.form["data"]})
		return json.dumps({"err":200,"err_msg":"Success"})
	else:
		return json.dumps({"err":201,"err_msg":"Parameter Missing"})

def worker():
	dict_a={"erase":erase,"backup":backup}
	while(True):
		req=inQ.get()
		dict_a[req["comm"]](req["data"])     
		print ("Command Executed")

if __name__ == '__main__':
	t=threading.Thread(target=worker)
	t.start()
	app.run("0.0.0.0",5000)




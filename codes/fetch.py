import requests
import time
import threading
from multiprocessing import Queue
import json
q=Queue()

def fetcher(data):
	r = requests.get(data)
	q.put(r.json())

counter=0
with open("sample.txt","r") as file:
	for x in file:
		counter+=1
		t=threading.Thread(target=fetcher,args=(x.rstrip(),))
		t.start()
result=[]
count=0
while(count<counter):
	result.append(q.get())
	count+=1
with open("outcome.json","w") as file:
	file.write(json.dumps(result,indent=4))

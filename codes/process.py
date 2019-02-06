from random import randint
import threading
import time
from multiprocessing import Queue,Process

def producer(a,myQ):
	while(True): # Runs forever
		myQ.put(a+": "+str(randint(0,999)))
		time.sleep(0.5)   # Sleeps to avoid using up CPU Cycles and Logically to delay execution

def consumer(name,myQ,outputQ):
	while(True):
		data=myQ.get() # Sleeps until any data is available in the Queue
		outputQ.put(data+name)

def output(outputQ):
	while(True):
		data=outputQ.get()+'\n'
		with open("log.log","a") as file:  # Logging to the file in sequential way
			file.write(data)



if __name__ == '__main__':
	myQ=Queue()   # Queue for Communication between producer and consumer
	outputQ=Queue() # Queue for communication between Consumer and output collector/ Logger
	t=Process(target=producer,args=("producer1",myQ,))
	t.start()
	t1=Process(target=consumer,args=("consumer1",myQ,outputQ))
	t1.start()
	t2=threading.Thread(target=output,args=(outputQ,))
	t2.start()



import requests
r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print (r.text)
print (r.json())

while(True):
	r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
	if(r.status_code!=200)
		print ("Server has issue")
	time.sleep(60)

# pip install requests    # For Access in Fidelity, You need proxy activated
import threading
import match
import errors
import dota2api as d2
import match_fetching
import os

import json

queue = []
tStatus = []

key1 = os.environ['D2_API_KEY'] 
key2 = os.environ['D2_API_KEY2'] 

class ThreadData:

	def __init__(self, ret, error):
		self.ret = ret
		self.error = error


def data_fetch(i, dEvent, api, base, cap, qLock):
	global queue

	matches = match_fetching.match_fetch(base, cap, api)

	qLock.acquire()
	queue.append(matches)
	dEvent.set()
	qLock.release()

	# Handle errorstStatus[0] = ThreadData(0,0)


def data_write(dEvent, qLock):
	global queue
	while(dEvent.wait()):
		qLock.acquire()
		data = queue.pop(0)

		qLock.release()

		# for i in data['matches']:
		# 	m = match.Match(data['matches'][i])
		# 	#do something with m


def main():
	global queueLock
	queueLock = threading.Lock()
	e = threading.Event()
	e.clear()
	api_1 = d2.Initialise(key1)

	t1 = threading.Thread(name='reading_1', target=data_fetch, kwargs=dict(i=0, dEvent=e, api=api_1, base=2000000000, cap=2000001000, qLock=queueLock))
	t2 = threading.Thread(name='writing_1', target=data_write, kwargs=dict(dEvent=e, qLock=queueLock))

	##loop
	while(True):

		if len(queue) == 0:
			dEvent.clear()
		if(not t1.is_alive()):
			pass

	t1.start()
	t2.start()

main()
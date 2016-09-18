import threading
import match
import errors
import dota2api as d2
import match_fetching
import os

from pprint import pprint

import json

queue = []

key1 = os.environ['D2_API_KEY'] 
key2 = os.environ['D2_API_KEY2'] 

def data_fetch(dEvent, api, base, cap, qLock):
	global queue

	matches = match_fetching.match_fetch(base, cap, api)

	qLock.acquire()
	queue.append(matches)
	dEvent.set()
	qLock.release()


def data_write(dEvent, qLock):
	global queue
	while(dEvent.wait()):
		qLock.acquire()
		data = queue.pop(0)
		if len(queue) == 0:
			#dEvent.clear()
			return
		qLock.release()

		for i in data['matches']:
			m = match.Match(data['matches'][0])
			#do something with m


def main():

	queueLock = threading.Lock()
	e = threading.Event()
	e.clear()
	api_1 = d2.Initialise(key1)

	t1 = threading.Thread(name='reading_1', target=data_fetch, kwargs=dict(dEvent=e, api=api_1, base=2000000000, cap=2000001000, qLock=queueLock))
	t2 = threading.Thread(name='writing_1', target=data_write, kwargs=dict(dEvent=e, qLock=queueLock))

	t1.start()
	t2.start()

main()
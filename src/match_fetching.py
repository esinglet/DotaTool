import dota2api as d2
# import mysql.connector as mdb #mariadb
import match
import pprint
from time import sleep

import json


def main():
	#Main function
	api = d2.Initialise()
	print(json.JSONEncoder().encode(match_fetch(2000000000, 2000001000, api)))


#Returns dictionary with 'matches' keyd to list of match dictionariesa
def match_fetch(base, cap, api):

	matches = {}
	matches['matches'] = []
	inc = 0 # Incriment

	while(True):
		try:
			dicti = api.get_match_history_by_seq_num(start_at_match_seq_num=base+inc, matches_requested=100)
			if (int(dicti['matches'][-1]['match_seq_num']) >= cap):
				#matches.extend(trim(dicti['matches'], cap))
				matches['matches'].extend(dicti['matches'])
				return matches
			else:
				matches['matches'].extend(dicti['matches'])
			inc = int(matches['matches'][-1]["match_seq_num"]) - base + 1
			sleep(1)
				
		except Exception as e:

			raise e

def test_unique(matches):
	res = True
	for i in matches:
		if (has_copy(i, matches)): 
			res = False
	return res

def has_copy(match, matches):
	count = 0
	for i in matches:
		if (i['match_seq_num'] == match['match_seq_num']):
			if (count == 0):
				count = 1
			else:
				print(i['match_seq_num']+' is duplicated.')
				return True
	return False

if __name__ == "__main__":
	main()

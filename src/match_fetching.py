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



def match_fetch(base, cap, api):

	# matches = []
	# inc = 0

	# for i in range(count): #Collect count x 100 matches

	# 	try:
	# 		dicti = api.get_match_history_by_seq_num(start_at_match_seq_num=base+inc, matches_requested=100)
	# 		matches.extend(dicti.get('matches'))
	# 		inc = int(matches[-1]["match_seq_num"]) - base + 1
	# 		sleep(2)
				
	# 	except Exception as e:
	# 		raise e

	# return matches #List of match dictionaries
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
			sleep(2)
				
		except Exception as e:
			raise e

def trim(matches, cap):
	old_split = 0
	split= len(matches) // 2 #Floor division
	ret = []

	if(matches[-1]['match_seq_num'] == cap):
		return matches[:-2]

	if(matches[split]['match_seq_num'] > cap): #Cut list below or at current split
		if ((split > 0) and (matches[split-1]['match_seq_num'] < cap)): #Cut list at
			return matches[:(split-1)]
		else: #Cut list below
			return trim(matches[:(split-1)], cap)
	elif(matches[split]['match_seq_num'] < cap): #Cut list above current split
		return matches[:(split-1)].extend(trim(matches[split:-1], cap))
	elif(matches[split]['match_seq_num'] == cap): #Cut list at and including current split and above
		return matches[:(split-1)]
	



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

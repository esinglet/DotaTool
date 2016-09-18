import dota2api as d2
# import mysql.connector as mdb #mariadb
import match
from time import sleep

import json


def main():
	#Main function
	match_fetch(5, 2000000000)



def match_fetch(count, base):

	api = d2.Initialise()
	matches = []
	inc = 0

	for i in range(count): #Collect count x 100 matches

		try:
			dicti = api.get_match_history()
			matches.extend(dicti.get('matches'))
			sleep(2)
				
		except Exception as e:
			raise e

	print(test_unique(matches))
	#print(json.dumps(matches))
	
	try:
		file = open('BatchData.json', 'w+')
		json.dump(matches, file)
		file.close()
	except:
		file.close()
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
				print(str(i['match_seq_num'])+' is duplicated.')
				return True
	return False

if __name__ == "__main__":
	main()

import dota2api as d2
from time import sleep

import json


def main():
	#Main function
	match_fetch()

api = d2.Initialise()

def match_fetch():

	api = d2.Initialise()

	
	input()

	for i in range(1):
		try:
			dicti = api.get_match_history_by_seq_num(start_at_match_seq_num=2000000000, matches_requested=2000)

			matches = (dicti.get('matches'))
			for match in matches:

				print(json.dumps(match, sort_keys=True,indent=15))
				sleep(1)
		except d2.src.exceptions.APIError as e:
			print(str(i)+" did not work.")

	input()

if __name__ == "__main__":
	main()

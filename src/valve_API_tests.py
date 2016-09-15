import dota2api as d2
from time import sleep
import json



def main():
#Needs enviroment variable set see wiki
	api = d2.Initialise()
	#print(api.get_match_details(1000193456))
	print(json.dumps(api.get_match_details(2000000774), sort_keys=True,indent=15))
	input()

main()




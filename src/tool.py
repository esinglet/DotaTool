import dota2api as d2
from json import dump


def main():
#Needs enviroment variable set see wiki
	api = d2.Initialise()

	value = input()

	if (value == 'hj'):
		try:
			
			file = open('heroes.json', 'w+')
			dump(api.get_heroes(), file)
			file.close()
		except  e:
			file.close()
			raise e
			sleep(10)
	elif (value == 'ht'):
		try:
			
			file = open('heroes.rtf', 'w+')
			dump(api.get_heroes(), file, sort_keys=True,indent=15)
			file.close()
		except  e:
			file.close()
			raise e
			sleep(10)

main()
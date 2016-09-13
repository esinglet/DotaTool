import dota2api as d2
import urllib.request
import json
import os
import re

from time import sleep



def main():
#Needs enviroment variable set see wiki
	api = d2.Initialise()
	urls = []
	value = input()

	#Make a heroes json file
	if (value == 'hj'):
		try:
			file = open('heroes.json', 'w+')
			json.dump(api.get_heroes(), file)
			file.close()
		except:
			file.close()
			raise e
			sleep(10)

	#Make a heroes formatted txt file
	elif (value == 'ht'):
		try:
			file = open('heroes.txt', 'w+')
			json.dump(api.get_heroes(), file, sort_keys=True,indent=15)
			file.close()
		except:
			file.close()
			raise e
			sleep(10)

	#Collect hero images 
	#Requires making a heroes json file first
	elif (value == "p"):
		try:
			fp = open('heroes.json', 'r+')
			jhero = json.load(fp)
			fp.close()

			for item in jhero["heroes"]:
				urls.append([ item["url_full_portrait"], item["url_large_portrait"], item["url_small_portrait"], item["name"]])

			if re.search(r"[a-zA-Z0-9]*\\src", os.getcwd()):
				os.chdir("..")
				if (not os.path.exists("res")):
					os.makedirs("res")
				os.chdir("res\\")

			if (not os.path.exists("portraits")):

				os.makedirs("portraits")
				os.makedirs("portraits\\large")
				os.makedirs("portraits\\small")

			for i in urls:
				urllib.request.urlretrieve(i[1], "portraits\\large\\"+i[3]+"-large.png")
				urllib.request.urlretrieve(i[2], "portraits\\small\\"+i[3]+"-small.png")

		except Exception as e:
			fp.close()
			raise e
			sleep(10)

main()

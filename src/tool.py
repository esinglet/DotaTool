import dota2api as d2
import urllib.request
import json
import os
import re
import sys

from time import sleep



def main():
#Needs enviroment variable set see wiki
	api = d2.Initialise()
	env = os.name
	pics = False

	while (True):
		
		print( 'hj = heros json')
		print( 'ht = heros text')
		print( 'p = heros pictures')
		print('q = quit')
		choice = input()

		#Make a heroes json file
		if (choice == 'hj'):
			try:
				file = open('heroes.json', 'w+')
				json.dump(api.get_heroes(), file)
				file.close()
			except:
				file.close()
				raise e
				sleep(10)

		#Make a heroes formatted txt file
		elif (choice == 'ht'):
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
		elif (choice == "p" and env == 'nt'):
			if (not pics):
				windowsFilesystemPicture()
				pics = True
			else:
				print("Refetch portraits? (y/n)")
				ans = input()
				if (ans == "y"):
					windowsFilesystemPicture()

			
		elif (choice == "p" and env == 'posix'):
			
			if (not pics):
				unixFilesystemPicture()
				pics = True
			else:
				print("Refetch portraits? (y/n)")
				ans = input()
				if (ans == "y"):
					unixFilesystemPicture()

		elif (choice == 'q'):
			quit()
		

def windowsFilesystemPicture():

	urls = []

	try:
		fp = open('heroes.json', 'r+')
		jhero = json.load(fp)
		fp.close()
	except Exception as e:
		try:
			fp.close()
		except:
			pass
		raise e
	
	for item in jhero["heroes"]:
		urls.append([ item["url_full_portrait"], item["url_large_portrait"], 
			item["url_small_portrait"], item["name"]])

	if re.search(r"[a-zA-Z0-9]*\\src", os.getcwd()):
		os.chdir("..")
		if (not os.path.exists("res")):
			os.makedirs("res")
		os.chdir("res/")

	if (not os.path.exists("portraits")):

		os.makedirs("portraits")
		os.makedirs("portraits\\large")
		os.makedirs("portraits\\small")

	for i in urls:
		urllib.request.urlretrieve(i[1], "portraits\\large\\"+i[3]+"-large.png")
		urllib.request.urlretrieve(i[2], "portraits\\small\\"+i[3]+"-small.png")

	#Reset for while loop and recalling
	os.chdir("../src")

def unixFilesystemPicture(fp):

	urls = []
	
	try:
		fp = open('heroes.json', 'r+')
		jhero = json.load(fp)
		fp.close()
	except Exception as e:
		try:
			fp.close()
		except:
			pass
		raise e

	for item in jhero["heroes"]:
		urls.append([ item["url_full_portrait"], item["url_large_portrait"], 
			item["url_small_portrait"], item["name"]])

	if re.search(r"[a-zA-Z0-9]*/src", os.getcwd()):
		os.chdir("..")
		if (not os.path.exists("res")):
			os.makedirs("res")
		os.chdir("res/")

	if (not os.path.exists("portraits")):

		os.makedirs("portraits")
		os.makedirs("portraits/large")
		os.makedirs("portraits/small")

	for i in urls:
		urllib.request.urlretrieve(i[1], "portraits/large/"+i[3]+"-large.png")
		urllib.request.urlretrieve(i[2], "portraits/small/"+i[3]+"-small.png")

	#Reset for while loop and recalling
	os.chdir("../src")

main()

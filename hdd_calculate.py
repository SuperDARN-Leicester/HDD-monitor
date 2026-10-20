#Program to find out how much HDD Space is left without deleting anything
# By Cassie Lakin
# 25-11-2025 V1.0

import shutil
import os
import datetime
#f = open("test.txt", "a") For test logging
#f.close()                 For test logging


def CALCULATE():
	global oldest_folder, percentage
	tot, usd, fre=shutil.disk_usage("/srv/")
	free = fre/1024**3  #
	total = tot/1024**3 # This formula converts the bytes to Gigabytes for easier reading.
	used = usd/1024**3  #
	percentage = (used/total)*100 # percentage of used space.

	print("The total space of storage drive is         ", total, "Gb")
	print("The total used space of storage drive is    ", used, "Gb")
	print("The total free space of storage drive is    ", free, "Gb\n")
	print("There is {:0.2f}%".format(percentage), "used")

	oldest_folder = sorted([ "/srv/data/borealis_data/"+f for f in os.listdir("/srv/data/borealis_data/")], key=os.path.getctime, reverse=False)[0]
	second_oldest_folder = sorted([ "/srv/data/borealis_data/"+f for f in os.listdir("/srv/data/borealis_data/")], key=os.path.getctime, reverse=False)[1]

	print ("the oldest file in the selected directory is: ",oldest_folder)
	print ("the next oldest file in the selected directory is: ",second_oldest_folder)
"""
try:
	CALCULATE()
	if percentage>65:
		print("delete delete delete")
		shutil.rmtree(oldest_folder)
		shutil.rmtree(second_oldest_folder)
	else:
		print("theres space left yet so no deletes")
except:
	print("finished")
"""
CALCULATE()

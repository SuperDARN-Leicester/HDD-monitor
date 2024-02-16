# Program to find out how much HDD Space is left before deleting oldest files
# By Cassie Lakin
# 9-2-2024 V1.0

import shutil
import os
import datetime
f = open("test.txt", "a")
f.close()
tot, usd, fre=shutil.disk_usage("/")
free = fre/1024**3  #
total = tot/1024**3 # This formula converts the bytes to Gigabytes for easier reading.
used = usd/1024**3  #
percentage = (used/total)*100 # percentage of used space.
#percentage = 80 # Test input

#print("The total space of drive c:     ", total, "Gb")
#print("The total used space of drive c:", used, "Gb")
#print("The total free space of drive c:", free, "Gb\n")
print("There is {:0.2f}%".format(percentage), "used")


oldest_file = sorted([ "d:/test_folder/"+f for f in os.listdir("d:/test_folder/")], key=os.path.getctime, reverse=True)[0]
#second_oldest_file = sorted([ "c:/users/cassi/PycharmProjects/file_space/venv/"+f for f in os.listdir("c:/users/cassi/PycharmProjects/file_space/venv/")], key=os.path.getctime)[1]

print ("the oldest file in the selected directory is: ",oldest_file)
#print ("the next oldest file in the selected directory is: ",second_oldest_file)
def FILE_REMOVE():
    #os.remove("test.txt")
    shutil.move(oldest_file, "C:/here/")

if percentage>=80:
    FILE_REMOVE()

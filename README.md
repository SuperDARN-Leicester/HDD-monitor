# HDD-monitor
HDD monitor and file moving
This python program will be run on a cronjob every hour. It is a very simple program in which it scans the hdd space of the drive that holds all the radar data. Once it has checked the drive it will either do nothing or delete the oldest files. If we decide to use more storage or another higher capacity drive it may move the file instead. This maybe altered if the latter is the case to delete old data from the second drive etc.

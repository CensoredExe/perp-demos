"""
Perpheads Demo Remover
This application will run in the background, and remove all your demos after a set time
To use this application, go to task manager, add this program to run on startup, and forget about it. It runs in the background, so nothing to fear!
"""
import os
import time
path = "D:/SteamLibrary/steamapps/common/GarrysMod/garrysmod/demos/" # Your perpheads demo's path
timedelete = 1 # How many days after the demos creation it gets deleted - Make sure its an integer
sleep = 30 # How many minutes the program sleeps for

seconds = timedelete*86400
demos = os.listdir(path)
for file in demos:
    timecreation = os.path.getctime(path + file)

    currenttime = time.time()
        
    #Check time since creation
    timesince = currenttime - timecreation
    days = timesince/86400
    if(timesince > seconds):
        try:
            os.remove(path + file)
            print(f"Deleted {file}, it has been {days} since creation")
        except:
            print(f"Error, could not delete {file}")
    else:
        print(f"{file} wasnt deleted, as its only been {days} since creation")

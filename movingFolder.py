import os
from distutils.dir_util import copy_tree
from osxmetadata import OSXMetaData, Tag
import osxmetadata
import json
import subprocess


# Getting the settings from json file
with open ("settings.json", "r") as read_file: 
    settings = json.load(read_file)


# Declaring source and destination folder
pathSource = settings['srcPath']
pathConvert = settings['dstPath']
iTunesPath = settings['itunesAutoPath']

#declaring tags object
m = settings['tagHasBeenMoved']
hasBeenMoved = [Tag(m)]



#Copying files
def copyFiles():
    subprocess.run(["clear"])
    print("starting the routine check")
    for root, dirs, files  in os.walk(pathSource, topdown=False):
        for name in dirs:

            folder = (os.path.join(root, name))

            md = osxmetadata.OSXMetaData(folder) 

            #next line is for testing purposes only, remove for build version
            #md.clear_attribute("tags")
            
            if not md.tags:
                #check if flac in folder
                print("new folders detected")
                if any(File.endswith('.flac') for File in os.listdir(folder)):
                    copy_tree(folder, pathConvert+"/"+name)
                    #add tag
                    md.tags+= hasBeenMoved
                    print(folder+" has been moved")
                
                elif any(File.endswith('.mp3') for File in os.listdir(folder)):
                    copy_tree(folder, iTunesPath)
                    md.tags+= hasBeenMoved
                    print("the folder "+name+" contained mp3 so it has been moved to  itunes already")
                    
            else: 
                print("nothing new to convert")
                return False

copyFiles()
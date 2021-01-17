import os
import logging
from distutils.dir_util import copy_tree
from osxmetadata import OSXMetaData, Tag
import osxmetadata
import json
import subprocess


# Getting the settings from json file
with open ("settings.json", "r") as read_file: 
    settings = json.load(read_file)


# Declaring source and destination folder
srcPath = settings['srcPath']
dstPath = settings['dstPath']
iTunesPath = settings['itunesAutoPath']

#declaring tags object
m = settings['tagHasBeenMoved']
hasBeenMoved = [Tag(m)]



#Copying files
def copyFiles():
    subprocess.run(["clear"])
    logging.info("starting the routine check")
    for root, dirs, files  in os.walk(srcPath, topdown=False):
        for name in dirs:

            folder = (os.path.join(root, name))

            md = osxmetadata.OSXMetaData(folder) 

            #next line is for testing purposes only, remove for build version
            md.clear_attribute("tags")
            
            if not md.tags:
                #check if flac in folder
                logging.info("new folders detected")
                if any(File.endswith('.flac') for File in os.listdir(folder)):
                    copy_tree(folder, dstPath+"/"+name)
                    #add tag
                    md.tags+= hasBeenMoved
                    logging.info(folder+" has been moved")
                
                elif any(File.endswith('.mp3') for File in os.listdir(folder)):
                    copy_tree(folder, iTunesPath)
                    md.tags+= hasBeenMoved
                    logging.info("the folder "+name+" contained mp3 so it has been moved to  itunes already")
                    
            else: 
                logging.info("nothing new to convert")
                return False

def controlPaths(): 
    if  not os.path.isdir(srcPath):
        logging.info("Error: the path" + srcPath + " specified for the srcPath in settings.json doesn't exist")
        logging.info("")
        logging.info("stopping process, please check your settings")
        exit()
    if  not os.path.isdir(dstPath):
        logging.info("Error: the path" + dstPath + " specified for the dstPath in settings.json doesn't exist")
        logging.info("")
        logging.info("stopping process, please check your settings")
        exit()
    if  not os.path.isdir(iTunesPath):
        logging.info("Error: the path" + iTunesPath + " specified for the itunesAutoPath in settings.json doesn't exist")
        logging.info("")
        logging.info("stopping process, please check your settings")
        exit()
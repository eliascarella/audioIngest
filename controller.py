import json
import os
import logging
from sys import exit
from convert import convert, addToLibrary
from movingFolder import copyFiles, controlPaths

#Get all paths from settings.json
with open("settings.json", "r") as read_file:
    settings = json.load(read_file)

srcPath = settings['srcPath']
dstPath = settings['dstPath']
iTunesPath = settings['itunesAutoPath']

def audioIngest():
#control that all paths exist
    controlPaths()
#copy the files to the temporary location
    copyFiles()
#once it's done, convert the files
    if not copyFiles():
        convert()
        addToLibrary()
import os
import json
import logging
from osxmetadata import OSXMetaData, Tag
import subprocess


# Getting the settings from json file
with open("settings.json", "r") as read_file:
    settings = json.load(read_file)

root = settings['dstPath']
iTunesPath = settings['itunesAutoPath']

# declaring tags object
c = settings['tagIsBeingConverted']
i = settings['tagHasBeenCopiedToLibrary']
hasBeenConverted = [Tag(c)]
hasBeenAdded = [Tag(i)]

# Iterate through files in all folders
def convert():
    for subdir, dirs, files in os.walk(root, topdown=False):
        for filename in files:
            inputFilePath = subdir + os.sep + filename

        # convert to mp3
            if inputFilePath.endswith(".flac"):
                logging.info('starting to convert '+ inputFilePath)
                filePath = inputFilePath.replace(".flac", "")
                outputFilePath = filePath + ".mp3"

                subprocess.run(["sox", inputFilePath, "-C 320", outputFilePath])

#open in iTunes
def addToLibrary():
    for subdir, dirs, files in os.walk(root, topdown=False):
        for filename in files:
            finalFile = subdir + os.sep + filename

            if finalFile.endswith(".mp3"):
                subprocess.run(["cp", finalFile, iTunesPath])
                logging.info("the file: "+finalFile+" has been added to the iTunes folder")

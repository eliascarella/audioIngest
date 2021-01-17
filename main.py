from convert import convert, addToLibrary
from movingFolder import copyFiles

#copy the files to the temporary location
copyFiles()

#once it's done, convert the files
if not copyFiles():
    convert()
    addToLibrary()
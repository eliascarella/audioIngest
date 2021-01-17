# audioIngest
Automatic audio file converter and ingester for iTunes
## about
### forewords
Started this project to learn python by doing a usefull set of actions. As of now it only converts .flac to 320CBR .mp3, I plan on adding all possible audio conversion possibilities later on. 
### Why would you need this ? 
If you use .mp3 for your itunes library but need to keep the original .flac files for, hmmm, _reasons_, then **this** is the tool for you ! 

This Daemon will routinely check for new folders of music and automatically convert them to 320CBR MP3 before adding the converted files to iTunes (using the "automatically add to iTunes" folder). If the files are already .mp3s they will swiftly be added to iTunes as well. 


## how it works
It leverages OSX's Tags attribute to keep a list of what has been processed and what hasn't.
Paths and Tags are storend in a settings.json, I'm implemented this right away for future GUI implementations. 


## Install
this project is OSX only and assumes that you have **SoX** and **LAME** binaries installed on your machine. 
It uses **python 3.7**

- clone this repo
- run ´git submodule init´
  - ´cd osxmetadata´
    - ´python setup.py install´


## Use
As of now there's only basic functionalities, star and/or watch this repo to know then the 1.0 will be out with a gui to dial-in the settings. 
If you want to try it out: **pre-tag the folders in the directory you want to be watched** so it doesn't get copied, converted and added into iTunes all over again. Use at your own risk.

## To-Do
by order of importance
- Delete copied and converted files at the end of the whole run
- daemonize the project
- Add multiple input/output type
- Basic GUI on mac menubar to check status, change settings. 
- multi-threading

#core libraries
import os
import time
import json
import logging
#local function
import controller
#external libraries
from daemonize import Daemonize

with open("settings.json", "r") as read_file:
    settings = json.load(read_file)


timeIntervalMinutes = settings['timeIntervalInMinutes']
timeInterval = round(int(timeIntervalMinutes)/0.016667)
startTime = time.time()

def main():
    while True:
        logging.info ("starting the process")
        controller.audioIngest()
        logging.info("")
        logging.info("Finished! I will try again in "+timeIntervalMinutes+" minutes.")
        time.sleep(timeInterval - ((time.time() - startTime) % timeInterval))

pid = "process/audioIngest.pid"
t = time.localtime()
currentTime = time.strftime("%H:%M:%S", t)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("./process/logs/audioIngest-"+currentTime+".log")
logger.addHandler(fh)

daemon = Daemonize(app="audio Ingest", pid=pid, action=main, foreground=True, verbose=True, keep_fds=fh.stream)
daemon.start()
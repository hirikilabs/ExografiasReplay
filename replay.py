#!/usr/bin/env python3
import time
import sys
import threading
import subprocess
import logging
from hank import Commands, Hank
from exocommands import command_times

END_TIME = 10


# help
def usage():
    print("Usage: ")
    print("\t", sys.argv[0], " <serial port> <video_file>")


def launch_video(video_file):
    subprocess.Popen(["/usr/bin/mpv", video_file], stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL)


def main():
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    # try to connect to hank
    hank = Hank(sys.argv[1])
    # if the connection is open process the list of commands
    if hank.is_open:
        while True:
            # create thread
            t = threading.Thread(target=launch_video, name="exovideo",
                                 args=[sys.argv[2]], daemon=True)
            t.run()
            logging.info("Starting...")
            # start at 0s time
            current_time = 0
            # get tuples of (time, command)
            for mov in command_times.items():
                # wait for command_time - current_time
                # (command times are absolute)
                time.sleep(mov[0]-current_time)
                # now we are at command_time
                current_time = mov[0]
                # send command
                logging.info(str(current_time) + ": Comando: "
                             + Commands.names[mov[1]])
                hank.send_command(mov[1])
            # wait a bit and start again
            time.sleep(END_TIME)
    else:
        print("Can't open serial port")
        sys.exit(1)


# entry point
if __name__ == "__main__":
    main()

import time
import sys
from hank import Commands, Hank
from exocommands import command_times


# help
def usage():
    print("Usage: ")
    print("\t", sys.argv[0], " <serial port>")


def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    # try to connect to hank
    hank = Hank(sys.argv[1])
    # if the connection is open process the list of commands
    if hank.is_open:
        while True:
            # start at 0s time
            current_time = 0
            # get tuples of (time, command)
            for mov in command_times.items():
                # wait for command_time - current_time (command times are absolute)
                time.sleep(mov[0]-current_time)
                # now we are at command_time
                current_time = mov[0]
                # send command
                print(current_time, ": Comando:", Commands.names[mov[1]])
                hank.send_command(mov[1])
            # wait a bit and start again
            time.sleep(5)
    else:
        print("Can't open serial port")
        sys.exit(1)


# entry point
if __name__ == "__main__":
    main()

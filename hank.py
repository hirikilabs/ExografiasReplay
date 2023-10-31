import time
import serial


# Class defining the commands available
class Commands:
    STOP = 0
    STEP_LEFT = 1
    STEP_RIGHT = 2
    WALK_LEFT = 3
    WALK_RIGHT = 4
    STAND_UP = 5
    SIT_DOWN = 6

    names = {0: "Stop", 1: "Step Left", 2: "Step Right", 3: "Walk Left",
             4: "Walk Right", 5: "Stand Up", 6: "Sit Down"}


# class defining the bytes we need to send over serial for each command
class SerialCommands:
    STOP = [144]
    STEP_LEFT = [169, 98]
    STEP_RIGHT = [169, 96]
    WALK_LEFT = [166, 160]
    WALK_RIGHT = [166, 161]
    STAND_UP = [208]
    SIT_DOWN = [224]


# class to interact with the exo
class Hank:
    COMMAND_WAIT = 3

    def __init__(self, serial_port):
        self.walking = False
        # try to open the serial port
        try:
            self.port = serial.Serial(serial_port, 921600)
            self.is_open = True
        except Exception as e:
            print("Can't open bluetooth: ", e)
            self.is_open = False

    def send_command(self, command):
        if self.is_open:
            # first check if we are walking as we need to send a stop
            # command if we are
            if self.walking and command != Commands.STOP:
                self.port.write(bytearray(SerialCommands.STOP))
                self.walking = False
                time.sleep(self.COMMAND_WAIT)
            # then process and send the command
            match command:
                case Commands.STOP:
                    self.port.write(bytearray(SerialCommands.STOP))
                    self.walking = False
                case Commands.STEP_LEFT:
                    self.port.write(bytearray(SerialCommands.STEP_LEFT))
                case Commands.STEP_RIGHT:
                    self.port.write(bytearray(SerialCommands.STEP_RIGHT))
                case Commands.SIT_DOWN:
                    self.port.write(bytearray(SerialCommands.SIT_DOWN))
                case Commands.STAND_UP:
                    self.port.write(bytearray(SerialCommands.STAND_UP))
                case Commands.WALK_LEFT:
                    self.walking = True
                    self.port.write(bytearray(SerialCommands.WALK_LEFT))
                case Commands.WALK_RIGHT:
                    self.walking = True
                    self.port.write(bytearray(SerialCommands.WALK_RIGHT))

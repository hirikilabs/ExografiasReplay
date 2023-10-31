from hank import Commands

# list of commands and the times we need to send them. (seconds : command)
command_times = {
    0: Commands.STAND_UP,
    32: Commands.SIT_DOWN,
    47: Commands.STAND_UP,
    58: Commands.WALK_LEFT,
    122: Commands.STOP,
    138: Commands.SIT_DOWN
}

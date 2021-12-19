import ctypes
from sys import argv
from time import sleep

## NOTE: This script will change your windows sensitivity. Some games uses their own sensitivity and will not be affected by the script.

# Change these keys to your fit
# Speed is between 1 and 20
SETTINGS = {
    'fast': 20,
    'slow': 1,
}
WAIT_TIME = 5 # Wait time before changing the sensitivity to normal

def change_speed(speed):
    set_mouse_speed = 113   # 0x0071 for SPI_SETMOUSESPEED
    ctypes.windll.user32.SystemParametersInfoA(set_mouse_speed, 0, speed, 0)
    print('Changed mouse sensitivty to {}'.format(speed))

def get_current_speed():
    get_mouse_speed = 112   # 0x0070 for SPI_GETMOUSESPEED
    speed = ctypes.c_int()
    ctypes.windll.user32.SystemParametersInfoA(get_mouse_speed, 0, ctypes.byref(speed), 0)

    return speed.value

if __name__ == "__main__":
    if (len(argv) > 1):
        setting = argv[1].lower()
        # Check if valid settings
        if setting in [i for i in SETTINGS]:
            # Get standard speed so we can reset it back
            standard_speed = get_current_speed()

            # Change the speed to the setting
            change_speed(SETTINGS[setting])

            # Wait x seconds and restore the sensitivty
            sleep(WAIT_TIME)
            change_speed(standard_speed)
        else:
            print('"{}" is not a valid setting\nAvailable settings:\nFAST\nSLOW'.format(setting))
    else:
        print('No setting were passed\nAvailable settings:\nFAST\nSLOW')
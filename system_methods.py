'''
This file contains all the system-y kid of functions
'''
import os
import time
import sys

####### CLEAR THE CONSOLE
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    
####### TYPE ONE LETTER AT A TIME

def delay_print(string):
    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0)

import os
import platform

def rerun():
    
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
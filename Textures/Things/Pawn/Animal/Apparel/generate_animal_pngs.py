import os
import shutil
from dictionaries import *

this_directory = os.path.dirname(os.path.abspath(__file__))
red_png = '/'.join([this_directory, 'red.png'])
blank_png = '/'.join([this_directory, 'blank.png'])

for name in animals:
    for blank in blank_files:
        print(blank)
        print(name)
        filename = '/'.join([this_directory, blank.format(name)])
        print(filename)
        if os.path.isfile(filename):
            print('File already exists.')
        else:
            print('File does not exist, creating now...')
            shutil.copy(blank_png,filename)

    for red in red_files:
        print(red)
        print(name)
        filename = '/'.join([this_directory, red.format(name)])
        print(filename)
        if os.path.isfile(filename):
            print('File already exists.')
        else:
            print('File does not exist, creating now...')
            shutil.copy(red_png,filename)

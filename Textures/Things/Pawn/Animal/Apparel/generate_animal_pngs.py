import os
from dictionaries import *

this_directory = os.path.dirname(os.path.abspath(__file__))

for name in animals:
    for red in red_files:
        print(red)
        print(name)

        filename = '/'.join([this_directory, red.format(name)])
        print(filename)
        if os.path.isfile(filename):
            print('file exists')
        else:
            print('file does not exist')

        input()
        # filename = red.format(animal_name=name)
        # file = os.commonpath(filename)
        # full_path = file.path
        # print(filename)
        # print(full_path)
    # for blank in blank_files:
    #     filename = red.format(name)
    #     print(filename)

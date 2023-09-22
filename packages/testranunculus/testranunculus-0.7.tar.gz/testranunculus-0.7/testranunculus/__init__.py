import os
import sys
# import all python files in the directory

# Get the path to the directory that contains your package
dir_path = os.path.dirname(os.path.realpath(__file__))
# import all python files in the directory
for file in os.listdir(dir_path):
    if file.endswith('.py') and file != '__init__.py':
        print(file)
        exec(f'from .{file[:-3]} import *')
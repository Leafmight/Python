from sys import argv
import csv
import platform
import argparse
import os.path
from os import path

import Solution_02_Exercise101 as my_func

def write_filenames_to_file(folderpath):
    entries = os.listdir(folderpath)
    my_func.write_list_to_file('csvfile.csv', entries)

#write_filenames_to_file(argv[1])

lst = []
def write_filenames_to_file_recursive(folderpath):
    entries = os.listdir(folderpath)
    for entry in entries:
        if os.path.isdir(entry):
            write_filenames_to_file_recursive(entry)
        else:
            lst.append(entry)

    my_func.write_list_to_file('csvfile.csv', lst)

#write_filenames_to_file(argv[1])
write_filenames_to_file_recursive(argv[1])
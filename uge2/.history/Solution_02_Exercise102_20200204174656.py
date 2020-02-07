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

write_filenames_to_file(argv[1])

folders = []
def write_filenames_to_file_recursive(folderpath):
    entries = os.listdir(folderpath)
    for entry in entries:
        if os.path.isdir(entry):
            write_filenames_to_file_recursive(entry)
    else:
        folders.append(entries)
    my_func.write_list_to_file('csvfile.csv', folders)

write_filenames_to_file(argv[1])
write_filenames_to_file_recursive(argv[1])
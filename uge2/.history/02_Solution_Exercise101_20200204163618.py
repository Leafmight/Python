from sys import argv
import csv
import platform
import argparse
import os.path
from os import path




def print_file_content(file):
    with open(file) as f_obj:
        content = f_obj.readlines()

    for line in content:
        print(line.strip().split(','))

def write_list_to_file(output_file, *lst):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    
    with open(output_file, 'w', newline=newline) as file:
        output_writer = csv.writer(file)
        for ele in lst:
            output_writer.writerow(ele)

def read_csv(file):
    with open(file) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())



def run():
    filename = argv[2]
    if argv[1]=="print_file_content":
        print_file_content(filename)
    if argv[1]=="write_list_to_file":
        inputlist = argv[3:]
        write_list_to_file(filename,inputlist)
    if argv[1]=="read_csv":
        read_csv(filename)


def run2():
    if args.exercise1:
        filename = argv[2]
        print_file_content(filename)
    if args.exercise2:
        filename = argv[2]
        inputlist = argv[3:]
        write_list_to_file(filename,inputlist)
    if args.exercise3:
        filename = argv[2]
        read_csv(filename)
    if args.file:
        if path.exists(argv[2]):
            filename = argv[2]
            inputlist = argv[3:]
            write_list_to_file(filename,inputlist)
        else:
            print("File doesn't exist: ", argv[2])



if __name__ == "__main__":
    parser = argparse.ArgumentParser(help="Handles Files")
    parser.add_argument("--exercise1", help="print file")
    parser.add_argument("--exercise2", nargs='*', help="Write to file")
    parser.add_argument("--exercise3",  help="print list")
    parser.add_argument("--file", nargs='*',  help="lol")
    args = parser.parse_args()
    run2()






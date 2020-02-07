from sys import argv
import csv
import platform

filename = argv[2]


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

def main():
    # print command line arguments
    if argv[1]=="print_file_content":
        print_file_content(filename)
    if argv[1]=="write_list_to_file"
        inputlist = argv[3:]
        write_list_to_file(filename,inputlist)

if __name__ == "__main__":
    main()
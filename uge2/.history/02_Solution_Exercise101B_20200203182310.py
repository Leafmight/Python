from sys import argv
import csv
import platform

filename1 = argv[1]
inputlist = argv[2:]
def write_list_to_file(output_file, *lst):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    
    with open(output_file, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        for ele in lst:
            output_writer.writerow(ele)
        
write_list_to_file(filename1,inputlist)
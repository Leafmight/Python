from sys import argv

filename = argv[1]
def print_file_content(file):
    with open(file) as f_obj:
        content = f_obj.readlines()

    for line in content:
        print(line.strip().split(','))

print_file_content(filename)




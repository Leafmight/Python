from sys import argv

filename = argv[2]
def print_file_content(file):
    with open(file) as f_obj:
        content = f_obj.readlines()

    for line in content:
        print(line.strip().split(','))



def main():
    # print command line arguments
    if argv[1]=="print_file_content":
        print_file_content(filename)
    


if __name__ == "__main__":
    main()
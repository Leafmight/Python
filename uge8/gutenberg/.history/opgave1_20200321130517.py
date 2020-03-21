import re

def gutenberg():
    with open("test.txt", 'r') as f:
        for line in f:
            print(line)

downloads_reg = re.compile(r'\d{} downloads')
gutenberg()
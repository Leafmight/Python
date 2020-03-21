import re

def gutenberg():
    with open("test.txt", 'r') as f:
        downloads_reg = re.compile(r'\d{} downloads')
        match_obj = downloads_reg.search(f)
        for line in f:
            print(line)

gutenberg()
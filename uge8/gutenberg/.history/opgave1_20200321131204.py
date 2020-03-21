import re

def gutenberg():
    with open("test.txt", 'r') as f:
        downloads_reg = re.compile(r'(\d+ downloads)')
        data = f.read()
        match_obj = downloads_reg.search(data)
        print(match_obj)

gutenberg()
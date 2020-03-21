import re

def gutenberg():
    with open("test.txt", 'r') as f:
        downloads_reg = re.compile(r'\d{} downloads')
        match_obj = downloads_reg.search(f)
        print(match_obj)

gutenberg()
import re

def gutenberg():
    with open("test.txt", 'r') as f:
        downloads_reg = re.compile(r'\d{} downloads')
        match_obj = downloads_reg.search("""hej 123 downloads""")
        print(match_obj)

gutenberg()
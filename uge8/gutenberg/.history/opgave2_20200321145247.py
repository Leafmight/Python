import urllib.request
import re

sherlock_urls = ['http://www.gutenberg.org/files/1661/1661-0.txt','http://www.gutenberg.org/files/2852/2852-0.txt',
'http://www.gutenberg.org/files/244/244-0.txt','http://www.gutenberg.org/files/2097/2097-0.txt',
'http://www.gutenberg.org/files/834/834-0.txt','http://www.gutenberg.org/files/108/108-0.txt',
'http://www.gutenberg.org/files/3289/3289-0.txt','http://www.gutenberg.org/files/2350/2350-0.txt',
'http://www.gutenberg.org/files/221/221-0.txt','http://www.gutenberg.org/ebooks/2347.txt.utf-8',
'http://www.gutenberg.org/ebooks/2346.txt.utf-8','http://www.gutenberg.org/ebooks/2344.txt.utf-8',
'http://www.gutenberg.org/ebooks/2343.txt.utf-8']

# for url in sherlock_urls:
#     with urllib.request.urlopen(url) as response:
#         html = response.read().decode('utf-8')

#         pound_reg = re.compile(r'[£] \d+|[£]\d+')
#         match_obj = pound_reg.findall(html)
#         print(match_obj)
with urllib.request.urlopen('http://www.gutenberg.org/files/1661/1661-0.txt') as response:
    html = response.read().decode('utf-8')
    pound_reg = re.compile(r'(\s+ [£] 4700 \s+)')
    match_obj = pound_reg.findall(html)
    print(match_obj)
# r'\n\n\w+ [£] 4700 \w+\n\n'

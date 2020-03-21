import urllib.request

sherlock_urls = ['http://www.gutenberg.org/files/1661/1661-0.txt','http://www.gutenberg.org/files/2852/2852-0.txt',
'http://www.gutenberg.org/files/244/244-0.txt','http://www.gutenberg.org/files/2097/2097-0.txt',
'http://www.gutenberg.org/files/834/834-0.txt','http://www.gutenberg.org/files/108/108-0.txt',
'http://www.gutenberg.org/files/3289/3289-0.txt','http://www.gutenberg.org/files/2350/2350-0.txt',
'http://www.gutenberg.org/files/221/221-0.txt','http://www.gutenberg.org/ebooks/2347.txt.utf-8',
'http://www.gutenberg.org/ebooks/2346.txt.utf-8','http://www.gutenberg.org/ebooks/2344.txt.utf-8',
'http://www.gutenberg.org/ebooks/2343.txt.utf-8']

with urllib.request.urlopen('http://python.org/%27') as response:
   html = response.read()
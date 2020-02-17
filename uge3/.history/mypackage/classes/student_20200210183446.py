import sys

print('__file__:{}\n__name__:{}\n__package__:{}\n'.format(__file__,__name__,str(__package__)))

class Student():
    """A Student"""

    def __init__(self, title, author, chapters=[]):
        """Initialize title, the author, and the chapters."""
        self.title = title 
        self.author = author
        self.chapters = chapters  

if __name__ == "__main__":
    print("hello in student")
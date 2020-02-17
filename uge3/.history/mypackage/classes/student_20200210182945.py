class Student():
    """A Student"""

    def __init__(self, title, author, chapters=[]):
        """Initialize title, the author, and the chapters."""
        self.title = title 
        self.author = author
        self.chapters = chapters  

if __name__ == "__main__":
    print("hello world")
def gutenberg():
    with open("test.txt", 'r') as f:
        for book in f:
            print(book)
gutenberg()
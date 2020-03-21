def gutenberg():
    with open("test.txt", 'r') as f:
        for lines in f:
            print(lines)
            print("---")
gutenberg()

def searcher():
    import time
    book="My name is Sumanta dey. And currenty studing b.tech degree "
    #consuming 4 sec delay
    time.sleep(4)

    while True:
        text=(yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in thee book.....")
search=searcher()
next(search)
search.send("name")
#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self.title=title
        self.page_count=(page_count)

    def turn_page(self):
        if isinstance(self.page_count,int):
            print("Flipping the page...wow, you read fast!")
        else:
            print("page_count must be an integer")

book = Book("The World According to Garp", 69)
book.turn_page()

    
        
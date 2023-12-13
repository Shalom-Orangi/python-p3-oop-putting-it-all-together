#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand=brand
        self.size=size
        self.condition="New"

    def check_size(self):
        if not isinstance(self.size,int):
            print("size must be an integer")  

    def repair (self):
        print("The shoe has been repaired")
        self.condition="New"

shoe= Shoe("Adidas",9)
shoe.check_size()
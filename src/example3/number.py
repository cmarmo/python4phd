## my first object-oriented modular python script

## The class Number

class Number:

    def __init__(self,num):

        self.num = num

    def square(self):

        n = self.num
        return n * n

    def cube(self):

        n = self.num
        return n*n*n


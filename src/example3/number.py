## my first object-oriented modular python script

## The class Number

class Number:

    def __init__(self,num):

        self.num = num

    def __square__(self):

        n = self.num
        return n * n

    def __cube__(self):

        n = self.num
        return n*n*n


## my first object-oriented python script

## The class Number
## https://docs.python.org/3.7/tutorial/classes.html
## Class definitions must be executed before they have any effect.

class Number:

    ## Instantiation method
    def __init__(self,num):

        ## num is an attribute of the class Number
        self.num = num

    ## Methods of the class Number

    def square(self):

        n = self.num
        return n * n

    def cube(self):

        n = self.num
        return n*n*n

## The main
def main():
    num = int(input("Please enter a number\n"))

    ## Class instantiation
    myNumber = Number(num)

    print(myNumber.square())
    print(myNumber.cube())

if __name__ == "__main__":
    main()


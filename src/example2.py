## my first object-oriented python script

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

## The main
def main():
    num = int(input("Please enter a number\n"))
    myNumber = Number(num)
    print(myNumber.square())
    print(myNumber.cube())

if __name__ == "__main__":
    main()


## my first object-oriented python script

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

## The main
def main():
    num = int(input("Please enter a number\n"))
    myNumber = Number(num)
    print(myNumber.__square__())
    print(myNumber.__cube__())

if __name__ == "__main__":
    main()


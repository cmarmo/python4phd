## my first object-oriented modular python script
from number import *

## The main
def main():
    num = int(input("Please enter a number\n"))
    myNumber = Number(num)
    print(myNumber.__square__())
    print(myNumber.__cube__())

if __name__ == "__main__":
    main()


## my first main with functions
## http://interactivepython.org/runestone/static/CS152f17/Functions/mainfunction.html

## Function definition
## Function definitions (def statements) must be executed before they have any effect.

def square(n):
    return n * n

def cube(n):
    return n*n*n


## The main function

def main():
    num = int(input("Please enter a number\n"))
    print(square(num))
    print(cube(num))

## https://docs.python.org/3.7/reference/executionmodel.html
## https://docs.python.org/3/library/__main__.html
## '__main__' is the name of the scope in which top-level code executes.
## __name__ is a built-in variable which evaluates to the name of the current module

if __name__ == "__main__":
    main()


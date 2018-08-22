## my first main with functions
## http://interactivepython.org/runestone/static/CS152f17/Functions/mainfunction.html

def square(n):
    return n * n

def cube(n):
    return n*n*n

def main():
    num = int(input("Please enter a number\n"))
    print(square(num))
    print(cube(num))

if __name__ == "__main__":
    main()


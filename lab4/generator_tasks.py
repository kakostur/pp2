#1
n=int(input())
def squre(n):
    for i in range(1,n+1):
        print(i*i) 
    
squre(n)

#2
def even_numbers(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num

def main():
    try:
        n = int(input())
        if n < 0:
            print()
            return

        even_nums = even_numbers(n)
        even_nums_str = ', '.join(map(str, even_nums))
        print(f"Even numbers between 0 and {n}:", even_nums_str)

    except ValueError:
        print()

if __name__ == "__main__":
    main()


#3
def divisible_by_3_and_4(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

def main():
    try:
        n = int(input())
        if n < 0:
            print()
            return

        generator = divisible_by_3_and_4(n)
        for num in generator:
            print(num)

    except ValueError:
        print()

if __name__ == "__main__":
    main()


#4
def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

def main():
    try:
        a = int(input())
        b = int(input())

        print(a, b)
        for square in squares(a, b):
            print(square)

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()


#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
def main():
    try:
        n = int(input())
        print( n)
        for num in countdown(n):
            print(num, end=" ")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()

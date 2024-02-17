#1
n=int(input())
def squre(n):
    for i in range(1,n+1):
        yield i*i 
    
squre_numbers=squre(n)
print(','.join(map(str, squre_numbers)))

#2
def even_numbers(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num

n=int (input())
num=even_numbers(n)
print(','.join(map(str,num)))

#3
def divisible_by_3_and_4(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

n=int(input())
numbers=divisible_by_3_and_4(n)
print(','.join(map(str,numbers)))


#4
def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a=int(input())
b=int(input())
sqr_numbers=squre(a,b)
print(','.join(map(str,sqr_numbers)))

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n=int(input())
nums=countdown(n)
print(','.join(map(str,nums)))
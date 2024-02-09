#1
# n=int(input())
# def calculate_factorial(n):
#     c=1
#     for i in range(1,n+1):
#         c*=i
#     return c
# print(calculate_factorial(n))

#2
# s=input()
# n=[]
# def reverse_string(s):
#     for i in range(len(s),0,-1):
#         n.append(s[i-1])
# reverse_string(s)
# print(''.join(n))

#3
# a=int(input())
# b=int(input())
# c=int(input())
# def getmax(a,b,c):
#     max1=a
#     if max1<b:
#         max1=b
#     if max1<c:
#         max1=c
#     return max1
# print(getmax(a,b,c))

#4
# n=int(input())
# def even(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")

# even(n)

#5
# n=int(input())
# arr=[]
# for i in range(0,n):
#     arr.append(int(input()))
# def arif(n):
#     s=0
#     a=0
#     for i in range(0,n):
#         s+=arr[i]
#         a=s/n
#     return a
# print(arif(n))


#6
# n=int(input())
# f=[0,1]
# def fib(n):
#     for i in range(2,n+1):
#         f.append(f[i-1]+f[i-2])
#     return f
# print (fib(n))
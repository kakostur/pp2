
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def count_primes(s):
    count = 0
    for num in s:
        if is_prime(num):
            count += 1
    return count
print(count_primes(arr))


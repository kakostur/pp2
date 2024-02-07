def histogram(int_list):
    for num in int_list:
        print('*' * num)

int_list = list(map(int, input().split()))

histogram(int_list)

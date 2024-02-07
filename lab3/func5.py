from itertools import permutations

def print_permutations(s):
    perms = permutations(s)
    for perm in perms:
        print(''.join(perm))

user_input = input()

print_permutations(user_input)

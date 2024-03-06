# m=input()
# def words(n):
#     for x in n:
#         yield x.upper()

# print(''.join(words(m)))



# from datetime import datetime, timedelta

# today= datetime.now()

# after=today + timedelta(days=100)
# print(after.strftime("%a"))




# import re
# pattern = re.compile(r'\+7\d{7}')
# n=input()
# print(pattern.search(n))


import re
n=input()
pattern = re.compile(r'\b\w*@email.com\b')
print(pattern.search(n))
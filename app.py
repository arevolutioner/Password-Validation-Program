"""
A program to check the validity of password input by users

A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z] At least 1 number between [0-9] At least 1 letter between [A-Z] At least 1 character
from [$#@] Minimum length of transaction password: 6 Maximum length of transaction password:
12 Your program should accept a sequence of comma separated passwords and will check them
according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comm

"""


import re
a = input('Enter passwords: ').split(',')
pass_pattern = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$")
for i in a:
    if pass_pattern.fullmatch(i):
        print(i)



# def is_low(x):
#     for i in x:
#         if "a" < i > "z":
#             return True
#     return False
#
#
# def is_up(x):
#     for i in x:
#         if "A" < i > "Z":
#             return True
#     return False
#
#
# def is_num(x):
#     for i in x:
#         if "0" < i > "9":
#             return True
#     return False
#
#
# def is_other(x):
#     for i in x:
#         if i=="$" and i=="#" and i=="@":
#             return True
#     return False
#
#
# password = input().split(",")
# lst=[]
#
# for i in password:
#     length=len(i)
#     if 7 < length > 13 and is_up(i) and is_low(i) and is_num(i) and is_other(i):
#         lst.append(i)


# print(lst)
#
# print(",".join(lst))


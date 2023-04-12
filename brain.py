import random
import string
from art import *

print("* Program for generating random passwords")
tprint('by Hhtitg1234')
print("version 1.0\n")
w = True
while w == True:
    print("""Select the desired option:
    1) Number password
    2) Number password with letters
    3) close program""")
    a = input("Enter the desired option number here: ")
    print()

    if a == '1':
        pol = int(input("Enter the number of characters in the password: "))
        print()
        pas = str('')

        while pol > 0:
            paas = str(random.randint(0, 9))
            pas += paas
            pol -= 1
        print("    * Your password: ", pas)
        print()
        pas = ''

    elif a == '2':
        s = int(input("Enter the number of characters in the password: "))
        print()
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=s))
        print("    * Your password: " + str(ran))
        print()

    elif a != '1' and a != '2' and a != '3':
        print("""Enter the desired option number!
        Example: 1; 2; 3
        """)

    elif a == '3':
        w = False
        break

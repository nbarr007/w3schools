import random


def nation_lottery1(name):
    print("Hello,", name, " your numbers are1: ", random.sample(range(0, 60), 6), "bonus", random.sample(range(0, 12), 2))


def nation_lottery2(name):
    print("Hello,", name, " your numbers are2: ", random.sample(range(0, 60), 6), "bonus", random.sample(range(0, 12), 2))


def nation_lottery3(name):
    print("Hello,", name, " your numbers are3: ", random.sample(range(0, 60), 6), "bonus", random.sample(range(0, 12), 2))


print('''
1.
2.
3. 
''')

question = input("What is your name: ")
name1 = question

option = int(input("Please select your option: "))
if option == 1:
    print(nation_lottery1(name1))
elif option == 2:
    print(nation_lottery2(name1))
elif option == 3:
    print(nation_lottery3(name1))












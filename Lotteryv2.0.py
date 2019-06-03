import random


def lottery(choice):
    if choice == '1':
        return 'Hello', capital.capitalize(), 'your Lotto numbers are:', random.sample(range(1,60),6)
    elif choice == '2':
        return 'Hello Your Euro Millions numbers are:', random.sample(range(1,51),5), 'your Lucky Stars numbers are:',random.sample(range(1,13),2)
    elif choice == '3':
        return 'Your Set For Life numbers are:', random.sample(range(1,48),5), 'your Life Ball number is:',random.sample(range(1,11),1)
    elif choice == '4':
        return 'Your Thunderball numbers are:', random.sample(range(1,40),5), 'your Thunderball number is:',random.sample(range(1,15),1)
    else:
        return 'please try again'


capital = input('What is your name: ')

pick = input('what is your choice: ')

result = lottery(pick)

print(result)







import random


def lotteryfull():
    print('Lotto')
    print('-----')
    print('Hello',  capital, 'your Lotto numbers are:', random.sample(range(1, 60), 6))
    print('Euro Millions')
    print('-------------')
    print('Your Euro Millions numbers are:', random.sample(range(1, 51), 5), 'your Lucky Stars numbers are:',random.sample(range(1,13),2))
    print('Set For Life')
    print('------------')
    print('Your Set For Life numbers are:', random.sample(range(1, 48), 5), 'your Life Ball number is:',random.sample(range(1,11),1))
    print('Thunderball')
    print('-----------')
    print('Your Thunderball numbers are:', random.sample(range(1, 40), 5), 'your Thunderball number is:',random.sample(range(1,15),1))


def lottery(choice):
    if choice == '1':
        return 'Hello',  capital, 'your Lotto numbers are:', random.sample(range(1, 60), 6)
    elif choice == '2':
        return 'Hello',  capital,'Your Euro Millions numbers are:', random.sample(range(1, 51), 5), 'your Lucky Stars numbers are:',random.sample(range(1,13),2)
    elif choice == '3':
        return 'Hello',  capital, 'Your Set For Life numbers are:', random.sample(range(1,48),5), 'your Life Ball number is:',random.sample(range(1,11),1)
    elif choice == '4':
        return 'Hello',  capital,'Your Thunderball numbers are:', random.sample(range(1,40),5), 'your Thunderball number is:',random.sample(range(1,15),1)
    elif choice == '5':
        return lotteryfull()
    else:
        return 'Please pick a number between 1 - 5: '


print("\n")

title = "Welcome to your national lottery number picker"
title1 ="===============================================\n\n"
title2 = '1. Lotto'
title3 = '2. Euro Millions'
title4 = '3. Set for life'
title5 = '4. Thunderball'
title6 = '5. The Full Monty'
print(title.center(148))
print(title1.center(152))
print(title2.center(142))
print(title3.center(150))
print(title4.center(150))
print(title5.center(148))
print(title6.center(152))


print("\n")
print("\n")

name = input("What is your name:  ")
pick = input('Please select your choice: ')

capital = name.capitalize()
result = lottery(pick)

print(result)





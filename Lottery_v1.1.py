import random


def lottery(choice):
    if choice == 1:
        return print('Hello',  capname, 'your Lotto numbers are:', random.sample(range(1,60),6))
    elif choice == 2:
        return print('Your Euro Millions numbers are:', random.sample(range(1,51),5), 'your Lucky Stars numbers are:',random.sample(range(1,13),2))
    elif choice == 3:
        return print('Your Set For Life numbers are:', random.sample(range(1,48),5), 'your Life Ball number is:',random.sample(range(1,11),1))
    elif choice == 4:
        return print('Your Thunderball numbers are:', random.sample(range(1,40),5), 'your Thunderball number is:',random.sample(range(1,15),1))
    else:
        print(1+2+3+4)


print("\n")

title = "Welcome to your national lottery number picker"
title1 ="===============================================\n\n"
title2 = '1. Lotto'
title3 = '2. Euro Millions'
title4 = '3. Set for life'
title5 = '4. Thunderball'
print(title.center(148))
print(title1.center(152))
print(title2.center(142))
print(title3.center(150))
print(title4.center(150))
print(title5.center(148))


print("\n")
print("\n")

name = input("What is your name:  ")
get = input('Please select your choice: ')

capname = name.capitalize()
chess = lottery(get)


print(chess)





def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."


get = input('what is your colour?  ')

while True:
    print('that is incorrect please try again')
    input('what is your choice')
    if get == 'red':
        break
    elif get == 'green':
        break
    elif get == 'bee purple':
        break

comment = commentary(get)

print(comment)
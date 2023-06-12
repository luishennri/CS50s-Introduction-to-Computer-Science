greeting = input("Greeting: ")

greeting = greeting.lstrip()

if greeting[0].lower() == 'h' and greeting[2].lower() == 'l':
    print('$0')
elif greeting[0].lower() == 'h' and greeting[2].lower() != 'l':
    print('$20')
else:
    print('$100')
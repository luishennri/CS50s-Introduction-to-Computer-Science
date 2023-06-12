while True:
    height = input('Height: ')
    if height > '0' and height <= '8':
        height = int(height)
        break
    else:
        continue

x = height -1

for i in range(1, height + 1):
    print(' ' * x + '#' * i + '  ' + '#' * i)
    x -= 1

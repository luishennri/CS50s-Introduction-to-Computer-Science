import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()
f = random.choice(fonts)

if len(sys.argv) == 0:
    f = random.choice(fonts)

else:
    if sys.argv[1] != '-f' and sys.argv[1] != '--font':
        print('Invalid usage')
        sys.exit(1)
    elif sys.argv[2] not in fonts:
        print('Invalid usage')
        sys.exit(1)
    else:
        f = sys.argv[2]

figlet.setFont(font=f)
text = input('Input: ')
print(figlet.renderText(text))
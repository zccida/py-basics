import sys
import pyfiglet
import random

'''
Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font,
in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and
the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
'''

pyfig_fonts = pyfiglet.FigletFont.getFonts()


if len(sys.argv) == 1:
    font_style = random.choice(pyfig_fonts)
    text_input = input("Input: ")
    word = pyfiglet.figlet_format(text_input, font=font_style)
    print(word)
elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in pyfig_fonts:
            font_style = sys.argv[2]
            text_input = input("Input: ")
            word = pyfiglet.figlet_format(text_input, font=font_style)
            print(word)
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")


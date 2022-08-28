import re

from colorama import Fore, Back, Style

text = input("Enter the text : ")

text1 = input("Enter the text to be highlighted : ")

if re.findall(text1, text):
    y = Fore.BLACK + Back.YELLOW + Style.BRIGHT + text1 + Style.RESET_ALL
    A = text.replace(text1, y)

    print(A)

else:
    print("Text is not present")

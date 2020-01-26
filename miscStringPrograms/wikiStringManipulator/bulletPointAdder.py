#! /usr/bin/env python

# This is a program that uses the pyperclip to paste content into the program
# and then formats the program and then copies the content back into the
# user's clipboard.

import pyperclip

unformattedText = pyperclip.paste()

# print(type(unformattedText))
listOfText = unformattedText.split()
# print(listOfText)

formattedText = []

for item in listOfText:
    formattedText.append('* ' + item + ('\n'))

stringifiedText = ''.join(formattedText)

pyperclip.copy(stringifiedText)

print(stringifiedText)


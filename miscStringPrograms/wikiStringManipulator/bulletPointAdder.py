#! /usr/bin/env python

# This is a program that uses the pyperclip to paste content into the program
# and then formats the program and then copies the content back into the
# user's clipboard.

import pyperclip

def pasteFromClipboard():
    unformattedText = pyperclip.paste()
    return unformattedText

def separateStrings():
    unformattedText = pasteFromClipboard()
    # print(type(unformattedText))
    listOfText = unformattedText.split()
    # print(listOfText)
    return listOfText

def formatStrings():
    listOfText = separateStrings()
    formattedList = []

    for item in listOfText:
        formattedList.append('* ' + item + ('\n'))

    formattedString = ''.join(formattedList)

    return formattedString


def copyToClipboard():
    formattedString = formatStrings()
    pyperclip.copy(formattedString)

    print(formattedString)

copyToClipboard()
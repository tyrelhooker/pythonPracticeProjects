#! python3.7

# advancedclipboard.py is a command line clipboard program that allows the user to save multiple items to the "clipboard", storing the items by a name, and then recall that item by entering the name into the the command line.

# Usage: python<versionNumber> advancedClipboard.py <userAction> <itemName>

import sys
import pyperclip

# TODO: Create check of command line items for sys.argv
# TODO: Create control for sys.argv[1] list that shows all names in shelve
# TODO: Create control for sys.argv[2] that saves argv[3] as key name
# TODO: Paste clipboard content to argv[2]'s value
clipboardContent = {}
if sys.argv[1] == 'save':
    clipboardContent[sys.argv[2]] = pyperclip.paste()
    print(clipboardContent)

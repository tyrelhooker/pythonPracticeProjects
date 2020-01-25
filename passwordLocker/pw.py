#! /usr/bin/env python

# py.py - This is an insecure password program to explore how password managers
# operate.

# Create executable commandline program to retrieve an account's password by
# typing in that account's name.

# 1. Create a dictionary to store PW by name: PW
# 2. Code to handle command line argument. Store the command line arguments
# in sys.argv.
import sys
import pyperclip


PASSWORDS = {
    'email': 'qwerty09876uiop12345',
    'todo_app': '54321asdfg67890hkll;',
    'comic_app': 'zxcvbnm,.0987612345'
}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]
noAccount = 'The account was not found.'

# pyperclip.copy(PASSWORDS.get(account, noAccount))
if account in PASSWORDS:
    print(f'The {account} name was found and the {account}\'s password has '
          f'been copied to your clipboard.')
    pyperclip.copy(PASSWORDS[account])
else:
    print(f'The {account} was not found.')





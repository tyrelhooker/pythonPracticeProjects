#! python3
# phoneAndEmailExtract.py - Finds phone numbers and emails from content
# copied to clipboard

import pyperclip
import re

# samplePhoneNumbers = ['8900988900', '123 456-7890', '234-567-8901',
#                       '(345) 678-9012', '456.789.0123', '555-555-5555 ext.80',
#                       '555-555-5555', 'testing this to see what kind of error I am re']
# sampleEmailAddresses = 'This string contains several test@gmail.com and yahoo@yahoo.com email addresses. I am testing to make sure single @ and .com are not caught as well as yahoo@ and @blank.com are not captured. If this works properly then testing@aol.com will be captured. And everything in "thisEmail@email.com" will also be captured.'

phoneNumRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\)|\[\d{3}\])?    # Area code (optional so uses ?)
    (\s|-|\.)?                      # Separator (optional so uses ?)
    (\d{3})                         # First three digits
    (\s|-|\.)                       # Separator (not optional so omits ?)
    (\d{4})                         # Last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Extension (optional so uses ?)
    )''', re.X)  # re.X is the same as re.VERBOSE

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.X)


copiedText = str(pyperclip.paste())
mo = phoneNumRegex.findall(copiedText)
mo2 = emailRegex.findall(copiedText)
numsAndEmails = []
copiedMessage = 'The following phone numbers and email addresses were copied to your clipboard:'
noMatchesMessage = 'No phone numbers or email addresses were found.'


for groups in mo:
    # Gathers and formats phone numbers according to one set standard.
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += f' x{groups[8]}'
    numsAndEmails.append(phoneNum)
for groups in mo2:
    numsAndEmails.append(groups[0])

if len(numsAndEmails) > 0:
    pyperclip.copy('\n'.join(numsAndEmails))
    print(copiedMessage)
    print(pyperclip.paste())
else:
    print(noMatchesMessage)

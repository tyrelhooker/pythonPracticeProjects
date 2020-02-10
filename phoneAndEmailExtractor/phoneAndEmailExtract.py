#! python3
# phoneAndEmailExtract.py - Finds phone numbers and emails from content
# copied to clipboard

import pyperclip
import re

samplePhoneNumbers = ['8900988900', '123 456-7890', '234-567-8901',
                      '(345) 678-9012', '456.789.0123', '555-555-5555 ext.80',
                      '555-555-5555', 'testing this to see what kind of error I am re']
sampleEmailAddresses = 'This string contains several test@gmail.com and yahoo@yahoo.com email addresses. I am testing to make sure single @ and .com are not caught as well as yahoo@ and @blank.com are not captured. If this works properly then testing@aol.com will be captured. And everything in "thisEmail@email.com" will also be captured.'

# Testing out the
# turned of soft wrap


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



# TODO: Find matches in clipboard text
copiedText = str(pyperclip.paste())
mo = phoneNumRegex.findall(copiedText)
mo2 = emailRegex.findall(copiedText)
numsAndEmails = []

# for i in range(len(mo2)):
#     # print(mo2[i][0])
#     numsAndEmails.append(str(mo2[i][0]))
#
# for i in range(len(mo)):
#     # print(mo2[i][0])
#     numsAndEmails.append(str(mo[i][0]))
#
# # print(numsAndEmails)
for groups in mo:
    # Gathers and formats phone numbers according to one set standard.
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += f' x{groups[8]}'
    numsAndEmails.append(phoneNum)

# # TODO: Copy results to the clipboard
#
# pyperclip.copy(str(numsAndEmails))


# mo = phoneNumRegex.findall(str(samplePhoneNumbers))
# print(type(mo))
# # print(type(mo) == list)
# if type(mo) == list:
#     phoneNumberList = ''
# for i in mo:
#     phoneNumberList += f'{i[0]}\n'
# print(phoneNumberList) else:
# print(mo)

# mo = phoneNumRegex.finditer(str(samplePhoneNumbers))
# print(type(str(samplePhoneNumbers)))
# print(mo['match'])

# phoneNumRegex = re.compile(r'((\d{3}|\(\d{3}\)|\[\d{3}\])?(\s|-|\.)?(\d{'
#                            r''r'3})(\s|-|\.)(\d{4}))', re.VERBOSE)
# mo = phoneNumRegex.findall(str(samplePhoneNumbers))
# # print(type(str(samplePhoneNumbers)))
# # print(type(mo))
# # for i in range(len(mo)):
# #     print(mo[i][0])
# print(list(filter(phoneNumRegex.match, samplePhoneNumbers)))

# for i in samplePhoneNumbers:
#     mo = phoneNumRegex.findall(i)
#     print(mo)
#     # for item in mo:
#     #     print(item[0])
# print(samplePhoneNumbers)

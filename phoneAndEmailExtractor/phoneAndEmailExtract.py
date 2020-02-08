import re

samplePhoneNumbers = ['8900988900', '123 456-7890', '234-567-8901', '(345) 678-9012',
                      '456.789.0123']

phoneNumRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\)|\[\d{3}\])?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    )''', re.X)  # re.X is the same as re.VERBOSE

mo = phoneNumRegex.findall(str(samplePhoneNumbers))
print(type(mo))
# print(type(mo) == list)
if type(mo) == list:
    phoneNumberList = ''
    for i in mo:
        phoneNumberList += f'{i[0]}\n'
    print(phoneNumberList)
else:
    print(mo)

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
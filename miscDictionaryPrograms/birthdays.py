# Check's user input against a prefilled birthday dictionary. If name is not
# in directory then it is added to the dictionary.
birthdays = {
    'Alice': 'Apr 1',
    'Bob': 'Dec 12',
    'Carol': 'Mar 4'
}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(f'{birthdays[name]} is the birthday of {name}')
    else:
        print(f'I do not have birthday information for {name}')
        print(f'What is {name}\'s birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthdays DB is updated.')

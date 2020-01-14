# A function that takes a list value as an argument and returns it as a
# string with all of the items separated by a comma, space, and an 'and'
# before the last item

def listToString(listValueName):
    stringList = ''
    for i in range(len(listValueName)):
        listValueName[i] = str(listValueName[i])
        if i == len(listValueName) - 1:
            stringList += 'and ' + listValueName[i]
        else:
            stringList += listValueName[i] + ', '
    print(stringList)

spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs', 1]

listToString(spam)

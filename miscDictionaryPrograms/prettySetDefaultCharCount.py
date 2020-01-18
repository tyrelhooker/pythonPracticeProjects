import pprint

message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ' \
          'pretium mattis dolor, ornare viverra ligula mollis ut.Donec ' \
          'suscipit massa. Lorem ipsum dol sit amet, consectetur adipiscing ' \
          'elit. Integer pretium mattis dolor, ornare viverra ligula mollis ' \
          'ut. Donec suscipit massa.'

count = {
    1: {
        'name': 'Testing',
        'object': 'out this nesting',
        'list': ['this', 'is', 'a', 'list', ['this', 'is', 'nested']],
        2: {'name': 'This is a further nested dict'}
    }
}

for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

# pprint.pprint(count)
# print(message)
print(count)
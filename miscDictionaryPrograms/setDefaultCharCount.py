message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ' \
          'pretium mattis dolor, ornare viverra ligula mollis ut. Donec ' \
          'suscipit massa. '

count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

print(count)
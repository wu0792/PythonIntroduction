friuts = ['apple','banana','water-melon','pear']

print('we have the following fruits:',friuts)

friuts.append('grape')

print('now we add grape, and now our fruits:',friuts)

del(friuts[0])
print('we delte the apple, and now our fruits:',friuts)

vocations = ('mon','tue','wed')

todo = ('finding the fruit',vocations,friuts)

print('the tuple todo is:',todo)

todo2 = ['another task is:',friuts,vocations]
print('the tuple todo2 is:',todo2)
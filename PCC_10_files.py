""" Python Crash Course Chapter 10 (Files)"""

# 10-1 Learning Python
filename = 'learning_python.txt'
#whole file
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#readlines
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

# list creation
with open(filename) as file_object:
    lines = file_object.readlines()
    text = []
    for line in lines:
        text.append(line.rstrip())

# list output
for i in text:
    print(f'Hey, {i}')

# 10-2 Learning C
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.replace('Python', 'C++').rstrip())

# 10-3 Guest
filename = 'guest.txt'
name = input('Enter your name: ')
with open(filename, 'w') as file_object:
    file_object.write(name)

# 10-4 Guest book
filename = 'guest_book.txt'
i = 0
while i < 10:
    prompt = ('Enter your name. Type "q" to quit.')
    name = input(prompt)
    if name == 'q':
        break
    message = ('Hello, ' + name + '! Nice to see you')
    print(message)
    message += '\n' 
    with open(filename, 'a') as file_object:
        file_object.write(message)
    i += 1

# 10-5 Poll

filename = 'poll.txt'
i = 0
while i < 10:
    prompt = ('Why you like programming?\n'
            'Type "q" to quit.\n')
    reason = input(prompt)
    if reason == 'q':
        break
    reason += '\n' 
    with open(filename, 'a') as file_object:
        file_object.write(reason)
    i += 1
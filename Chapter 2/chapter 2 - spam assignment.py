spam = 0
print('Hello, please put in a number to see what spam says')
playerInput = input()
if playerInput == '1':
    spam = spam + 1
    print('Hello')
elif playerInput == '2':
    spam = spam + 2
    print('Howdy')
else:
    print('Greetings!')
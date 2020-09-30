import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    else:
        print('You typed ' + response +'.')
        break
print('You exited out the while loop you cheater, now While = False, go back and start the program again')
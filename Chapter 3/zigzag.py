import time, sys
indent = 0 #How many spaces to indent
indentIncreasing = True #Whether the indentiation is increasing or not

try:
    while True: #The main program loop
        print(' '* indent, end='') #This end prevents a new line to start for the next print function
        print('********')
        time.sleep(0.1) #Pause for 1/10 second

        if indentIncreasing:
            #Increase the number of spaces
            indent = indent + 1
            if indent == 20:
                #Change direction:
                indentIncreasing = False

        else:
            #Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                #Change direction:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
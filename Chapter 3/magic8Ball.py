import random #imports the random module

def getAnswer(answerNumber): #getAnswer() function is defined
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9) #random.randint function is called with two arguments: 1 and 9
fortune = getAnswer(r) #random integer between 1 and 9 (including 1 and 9 themselves) is stored in a variable named r, getAnswer() function is called
print(fortune) #returned string is assigned to string ^ and passed to print() cal where it is printed to the screen
def spam():
    global eggs
    eggs = 'spam' #this is global because global assignment

def bacon():
    eggs = 'bacon' #this is local because its an assignment statement

def ham():
    print(eggs) #this is global because there is no assignment statement or global statement

eggs = 42 #this is global
spam()
print(eggs)
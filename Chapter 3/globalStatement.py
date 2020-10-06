def spam():
    global eggs #global tells Python don't create a local variable with this name.
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

#output is spam beecause eggs is declared global at the top of spam, so when eggs is set to 'spam', this assignment is done to the globally scoped eggs. (replacing global to spam)
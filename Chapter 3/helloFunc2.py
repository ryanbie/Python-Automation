def hello(name): #parameter called name (parameters are variables that contain arguments)
    print("Hello " + name)

hello('Alice')
hello('Bob')

#Note: The value stored in parameters is forgotten when the function returns
#To define a function is to create it, just like an assignment statement like spam = 42 creates the spam variable.
#The def statement defines the sayHello() function
#➊. The sayHello('Al') line
#➋ calls the now-created function, sending the execution to the top of the function’s code.
#This function call is also known as passing the string value 'Al' to the function.
#A value being passed to a function in a function call is an argument.
#The argument 'Al' is assigned to a local variable named name.
#Variables that have arguments assigned to them are parameters.
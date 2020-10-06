def a():
    print('a() starts')

    b()
    d()
    print('a()returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()

#The call stack is how Python remembers where to return the exectuion after each function call.
#Python creates a frame object on the top of the call stack, which stores the line number of the original function call so Python can remember where to return.
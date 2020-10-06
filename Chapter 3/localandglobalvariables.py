def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

#eggs will still print 99 because eggs is a local variable in the local scope
#parameters and variables that are assigned in a called function are said to exist in that function's local scope.
#variables that are assigned outside of all functions are said to exist in the global scope
#a variable that exists in a local scope is a local variable, while a variable that exists in the global scope is a global variable.
#a variable must be one or the other, it cannot be both (local and global variable).es are forgotten. The next time you call the function, the local variables will not remember the values stored in them from the last time the function was called.
#think of a scope as a container for variables
#A local scope is created whenever a function is called. Any variables assigned in the function exist within the function’s local scope. When the function returns, the local scope is destroyed, and these variabl
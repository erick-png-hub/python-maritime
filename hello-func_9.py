globalVar = 'I am global'

def myFunction():
    global globalVar
    globalVar = 'I changed it!'
    print(globalVar)

myFunction()
print(globalVar)
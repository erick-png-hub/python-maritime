globalVar = 'I am global'

def myFunction():
    globalVar = 'I changed it'
    print(globalVar)

myFunction()
print(globalVar)
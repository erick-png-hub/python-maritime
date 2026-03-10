# This program says hello and asks for my name.

print('Hello, world!')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

#Questions:

#1
# *, -, /, +, are operators in Python. They are used to perform mathematical operations on numbers.

# 'hello' , -88.8, 5 are operands in Python. They are the values that the operators operate on.

#2
#spam is avariable, while 'spam' is a string literal.

#3
#Datatypes in Python include:
#1. int - for whole numbers
#2. float - for decimal numbers
#3. str - for text
#4. bool - for True/False values    

#4
#An expression is a combination of values and operators that can be evaluated to produce a result. For example, 2 + 3 is an expression that evaluates to 5.

#5
#A statement is a line of code that performs an action. For example, print('Hello, world!') is a statement that prints the text 'Hello, world!' to the console.
#The difference between an expression and a statement is that an expression produces a value, while a statement performs an action.

#6
#Why is eggs a valid variable name while 100 is invalid?
#Eggs is a valid variable name because it starts with a letter and does not contain any spaces or special characters. 100 is an invalid variable name because it starts with a number, which is not allowed in Python variable names.

#7
#What three functions can be used to get the integer, floating-point number, or string version of a value?
#The three functions are int(), float(), and str() respectively. They can be used to convert a value to the desired data type. For example, int('5') will convert the string '5' to the integer 5, float('3.14') will convert the string '3.14' to the floating-point number 3.14, and str(10) will convert the integer 10 to the string '10'.

#8
#Why does this expression cause an error? How can you fix it?
#The expression 'I have eaten ' + 99 + ' burritos.' causes an error because it is trying to concatenate a string ('I have eaten ') with an integer (99) and another string (' burritos.'). In Python, you cannot concatenate a string with an integer directly. To fix this, you can convert the integer to a string using the str() function. The corrected expression would be 'I have eaten ' + str(99) + ' burritos.' which will produce the output 'I have eaten 99 burritos.'.

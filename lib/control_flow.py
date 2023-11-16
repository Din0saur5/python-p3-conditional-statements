#!/usr/bin/env python3

def admin_login(username, password):
    check_user = username.upper() 
    if check_user == 'ADMIN' and password == '12345':
       return 'Access granted'
    else:
        return 'Access denied'

def hows_the_weather(temperature):
    if temperature<40:
        return "It's brisk out there!"
    elif temperature >=40 and temperature<65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    if num%3 + num%5 == 0:
        return 'FizzBuzz' 
    elif num%3 ==0:
        return 'Fizz'
    elif num%5 == 0:
        return 'Buzz'
    else:
        return num

def calculator(operation, num1, num2):
    if operation == '+':
        solution =add(num1,num2)
    elif operation == '-':
        solution =sub(num1,num2)
    elif operation == '*':
        solution =mult(num1,num2)
    elif operation == '/':
        solution =div(num1,num2)
    else:
        print('Invalid operation!')
        solution = None
    return solution
    
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mult(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
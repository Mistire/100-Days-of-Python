from art import logo
import os

def add (n1, n2):
  return n1 + n2
def substract (n1, n2):
  return n1 - n2
def multiply (n1, n2):
  return n1 * n2
def divide (n1, n2):
  return n1 / n2

operations = {'+':add, '-':substract, '*':multiply, '/':divide}



def calculator():
  print(logo)
  num1 = float(input("What's the first number: "))
  for operation in operations:
    print(operation)
  calculating = True

  while calculating:
    operation_symbol = input("Pick an operation from the above line: ")
    num2 = float(input("What is the next number: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")


    if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      calculating = False
      os.system('cls')
      calculator()

calculator()
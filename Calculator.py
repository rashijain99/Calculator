print(" Calculator ")

def add(a,b):
     return a+b

def sub(a,b):
     return a-b

def mul(a,b):
     return a*b

def div(a,b):
     return a/b

print("select operation")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.divide")

while True:
     operation = input("select (1/2/3/4) : ")

     if operation in ('1', '2', '3', '4'):
          num1: float = float(input("Enter first number: "))
          num2: float = float(input("Enter second number: "))

          if operation == '1':
             print("num1", "+", "num2" " " "is", add(num1, num2))

          elif operation == '2':
             print("num1", "-", "num2" " " "is", sub(num1, num2))

          elif operation == '3':
             print("num1", "*", "num2" " " "is",  mul(num1, num2))

          elif operation == '4':
             print("num1", "/", "num2" " " "is", div(num1, num2))

          next_calculation = input("Let's do next calculation? (yes/no): ")
          if next_calculation == "no":
             break

     else:
        print("invalid operation")
        break
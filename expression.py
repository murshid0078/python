expression = input("Enter a mathematical expression to solve: ")

try:
    result = eval(expression)
    print(f"The result is: {result}")
except Exception as e:
    print(f"Error in evaluating the expression: {e}")
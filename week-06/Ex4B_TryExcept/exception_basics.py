# ValueError happens when the correct type is used but the value itself is invalid.
try: 
    number = int("hello")

except ValueError:
    print("ValueError: Cannot convert text into an integer.")

else:
    print(number)

finally:
    print("Let's try another one...\n")

# NameError happens when Python cannot recognize a variable of object name.
try:
    m = banana 

except NameError:
    print("NameError: Undefined variable used.")

else:
    print(m)

finally:
    print("Let's try another one...\n") 

# TypeError happens when incompatible data types are used together. 
try:
    result = 5 + "apple"

except TypeError:
    print("TypeError: Cannot combine integer and string.")

else:
    print(result)

finally:
    print("Let's try another one...\n")

# SyntaxError happens when Python code is written with invalid syntax.
try:
    eval("if True print('hello')")

except SyntaxError:
    print("SyntaxError: Invalid syntax used.")

else:
    print("No syntax error.")

finally:
    print("Let's try another one...\n")
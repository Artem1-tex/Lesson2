number1 = int(input("введіть перше число:"))
number2 = int(input("введіть друге число:"))
action = input("Введіть дію (+, -, *, /):")

if action == "+":
    print("Відповідь:", number1 + number2 )
elif action == "-":
    print("Відповідь:", number1 - number2)
elif action == "*":
    print("Відповідь:", number1 * number2)
elif action == "/":
    if number2 == 0:
        print("Ділення на нуль неможливо!")
    else:
        print("Відповідь:", number1 / number2)
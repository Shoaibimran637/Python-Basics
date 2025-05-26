# Perform calculations based on user choice
if operation == "Adn":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "Sbn":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "Dvn":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
elif operation == "Mlt":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
else:
    print("Invalid operation. Please enter Adn, Sbn, Mlt, Dvn")

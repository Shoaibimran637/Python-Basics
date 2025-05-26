# Temperature Converter
temp_type = input("Enter type of temperature (Celsius / Fahrenheit): ").lower()
temp_val = float(input("Enter the temperature value: "))
if temp_type == "celsius":
    fahrenheit = (temp_val * 9/5) + 32
    print(f"The temperature in Fahrenheit is {fahrenheit}")
elif temp_type == "fahrenheit":
    celsius = (temp_val - 32) * 5/9
    print(f"The temperature in Celsius is {celsius}")
else:
    print("Invalid temperature type.")

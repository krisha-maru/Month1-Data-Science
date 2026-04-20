def celsius_to_fahrenheit(temp_list):
    converted = []
    for temp in temp_list:
        converted.append((temp * 9/5) + 32)
    return converted

celsius_values = [0, 20, 30, 40]
fahrenheit_values = celsius_to_fahrenheit(celsius_values)
print("Celsius values:", celsius_values)
print("Fahrenheit values:", fahrenheit_values)
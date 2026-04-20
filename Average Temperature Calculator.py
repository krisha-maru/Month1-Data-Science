def calculate_average_temperature(temps):
    if len(temps) == 0:
        return 0 
    else:
        return sum(temps) / len(temps)
temps = [float(x) for x in input('Enter the temperatures separated by commas: ').split(',')]
avg_temp = calculate_average_temperature(temps)
print(f'The average temperature is {avg_temp: .3f} degrees.')

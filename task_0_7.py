def celsius_to_fahrenheit(temperature):
    formula = (temperature*1.8) + 32
    return float(formula)

def fahrenheit_to_celsius(temperature):
    formula = (temperature-32)/1.8
    return float(formula)


print(str(celsius_to_fahrenheit(32)))
print(str(fahrenheit_to_celsius(89.6)))
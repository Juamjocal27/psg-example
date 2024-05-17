celsius = 30

def temperatura(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

print(temperatura(30))
print(temperatura(-273.99))
print(temperatura(100))
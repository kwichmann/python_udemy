def celsius_to_fahrenheit(c):
    if (c < -273.15):
        return "Temperature below absolute zero"
    f = c * 1.8 + 32
    return f

def fahrenheit_to_celsius(f):
    if (f < -459.67):
        return "Temperature below absolute zero"
    c = (f - 32) / 1.8
    return c

temperatures = [10,-20,-289,100]

for t in temperatures:
    print(celsius_to_fahrenheit(t))
    
with open("temperatures.txt", "w") as file:
    for t in temperatures:
        if t > -273.15:
            file.write(str(celsius_to_fahrenheit(t)) + "\n")
#__init__
from .celsius_to_fahrenheit import celsius_to_fahrenheit
from .fahrenheit_to_celsius import fahrenheit_to_celsius
from .celsius_to_kelvin import celsius_to_kelvin


#celsius_to_fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


#fahrenheit_to_celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

#celsius_to_kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15


#main.py
from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin

def main():
    print("Temperature Conversion Options:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {celsius_to_fahrenheit(celsius)}°F")
    
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit)}°C")
    
    elif choice == 3:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {celsius_to_kelvin(celsius)}K")
    
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()=
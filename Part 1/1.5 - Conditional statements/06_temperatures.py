# Write your solution here
fahrenheit = int(input("Please type in a temperature (F): "))
celcius = (fahrenheit - 32) * 5/9

if celcius < 0:
    print(f"{fahrenheit} degrees Fahrenheit equals {celcius} degrees Celsius")
    print("Brr! It's cold in here!")

if celcius >= 0: 
    print(f"{fahrenheit} degrees Fahrenheit equals {celcius} degrees Celsius")

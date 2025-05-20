def convert_fahrenheit_in_celsius():
    value_fahrenheit=float(input("Enter value in Fahrenheit : "))
    value_celsius=(value_fahrenheit-32)*5.0/9.0
    print(f"{value_fahrenheit}F = {value_celsius}C ")

if __name__=="__main__":
    convert_fahrenheit_in_celsius()
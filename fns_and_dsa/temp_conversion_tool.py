FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    return (float(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR)
def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    return (float(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32)
input_temperature = float(input("Enter the temperature to convert: "))
input_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if input_unit == 'C':
    converted_temperature = convert_to_fahrenheit(input_temperature)
    print(f"{input_temperature}°C is {converted_temperature}°F")
elif input_unit == 'F':
    converted_temperature = convert_to_celsius(input_temperature)
    print(f"{input_temperature}°F is {converted_temperature}°C")
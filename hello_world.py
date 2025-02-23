print("Hello World!")
home = 'My Family House'
Work = 'My office'


# temperature.py

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

# utilities/math_operations.py

import math

def square_root(value):
    """Returns the square root of a number."""
    return math.sqrt(value)

def power(base, exponent):
    """Returns the base raised to the exponent."""
    return math.pow(base, exponent)

# utilities/string_operations.py

def reverse_string(s):
    """Returns the reversed string."""
    return s[::-1]

def to_uppercase(s):
    """Converts a string to uppercase."""
    return s.upper()

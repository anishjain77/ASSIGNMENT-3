import math

# Ask the user for a number
num = float(input("Enter a number: "))

# Calculate using math module
sqrt_value = math.sqrt(num)
log_value = math.log(num)
sine_value = math.sin(num)

# Display the results
print("Square root of", num, "is:", sqrt_value)
print("logarithm ", num, ":", log_value)
print("Sine of", num, "is:", sine_value)

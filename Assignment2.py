# 1. Create variables to store your name, age, and whether you’re a student (bool).
name = "Shravani"
age = 20
is_student = True

# 2. Print out the type of each variable.
print(type(name))       # Output: <class 'str'>
print(type(age))        # Output: <class 'int'>
print(type(is_student)) # Output: <class 'bool'>

# 3. Convert a string number (e.g., "45") to an integer and add 10.
string_number = "45"
converted_number = int(string_number) + 10
print(converted_number)  # Output: 55

# 4. Try converting a float to an integer and print the result.
float_number = 12.7
converted_float = int(float_number)
print(converted_float)   # Output: 12

# 5. Use type() to check the type of a variable after type conversion.
print(type(converted_number))  # Output: <class 'int'>
print(type(converted_float))   # Output: <class 'int'>


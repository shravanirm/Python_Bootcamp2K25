# -------------------------------
# 1. Number Sign Checker
# -------------------------------
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print("\n" + "-"*30 + "\n")

# -------------------------------
# 2. Driving Eligibility
# -------------------------------
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible for Driving License")
else:
    print("Not Eligible")

print("\n" + "-"*30 + "\n")

# -------------------------------
# 3. Grading System
# -------------------------------
marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

print("\n" + "-"*30 + "\n")

# -------------------------------
# 4. Nested Login Check
# -------------------------------
is_logged_in = True
is_admin = False

if is_logged_in and is_admin:
    print("Welcome Admin")
elif is_logged_in:
    print("Welcome User")
else:
    print("Please log in")

print("\n" + "-"*30 + "\n")

# -------------------------------
# 5. Max of 3 Numbers
# -------------------------------
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number is:", largest)

print("\n" + "-"*30 + "\n")

# -------------------------------
# 6. Even or Odd Checker
# -------------------------------
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

print("\n" + "-"*30 + "\n")

# -------------------------------
# 7. Password Validator
# -------------------------------
password = input("Enter password: ")
if password == "admin123":
    print("Access Granted")
else:
    print("Access Denied")

print("\n" + "-"*30 + "\n")

# -------------------------------
# 8. Leap Year Checker
# -------------------------------
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

print("\n" + "-"*30 + "\n")

# -------------------------------
# 9. Temperature Converter
# -------------------------------
temp = float(input("Enter temperature: "))
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()

if unit == "C":
    f = (temp * 9/5) + 32
    print(f"{temp}°C = {f:.2f}°F")
elif unit == "F":
    c = (temp - 32) * 5/9
    print(f"{temp}°F = {c:.2f}°C")
else:
    print("Invalid unit")

print("\n" + "-"*30 + "\n")

# -------------------------------
# 10. Rock, Paper, Scissors Game (1-Player)
# -------------------------------
import random

choices = ["rock", "paper", "scissors"]
user_choice = input("Enter rock, paper, or scissors: ").lower()
computer_choice = random.choice(choices)

print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")

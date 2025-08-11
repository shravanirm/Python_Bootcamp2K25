# Reverse Countdown Timer
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i)

# Break the Loop on Password Match
while True:
    pwd = input("Enter password: ")
    if pwd == "python123":
        print("Password matched!")
        break
    else:
        print("Wrong password, try again.")

# Count Vowels in a Word
word = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0
for ch in word:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)

# Print All Odd Numbers Between 1 and 50
for i in range(1, 51):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# Factorial Calculator
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

# Print Numbers 1 to 10 (while loop)
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()

# Countdown Program (while loop)
n = int(input("Enter a number: "))
while n > 0:
    print(n, end=" ")
    n -= 1
print()

# Multiplication Table (1 to 10)
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Skip Multiples of 3
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# First 5 Even Numbers
count = 0
i = 1
while True:
    if i % 2 == 0:
        print(i, end=" ")
        count += 1
        if count == 5:
            break
    i += 1

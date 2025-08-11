# 1. Loop through a Tuple
movies = ("Inception", "Interstellar", "The Dark Knight", "Avengers: Endgame", "Titanic")
print("Favorite Movies:")
for movie in movies:
    print(movie)
print("-" * 40)

# 2. Use enumerate() with a List
fruits = ["Apple", "Banana", "Cherry", "Mango", "Grapes"]
print("Fruits with Index:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
print("-" * 40)

# 3. Use .items() on a Dictionary
students = {"Alice": 85, "Bob": 92, "Charlie": 78}
print("Students and Grades:")
for student, grade in students.items():
    print(f"{student}: {grade}")
print("-" * 40)

# 4. Use .values() on a Dictionary
countries = {"India": "New Delhi", "USA": "Washington D.C.", "Japan": "Tokyo"}
print("Capitals Only:")
for capital in countries.values():
    print(capital)
print("-" * 40)

# 5. Loop through a Set
animals = {"Dog", "Cat", "Elephant", "Tiger", "Zebra"}
print("Animal Names:")
for animal in animals:
    print(animal)
print("-" * 40)

# 6. Loop Through Dictionary Keys Only
products = {"Pen": 10, "Notebook": 40, "Eraser": 5}
print("Product Names:")
for product in products.keys():
    print(product)
print("-" * 40)

# 7. Loop with range() to Generate Even Numbers
print("First 10 Even Numbers:")
for num in range(2, 21, 2):
    print(num)
print("-" * 40)

# 8. Loop Through Nested Dictionary
students_nested = {
    "Amit": {"age": 20, "grade": "A"},
    "Riya": {"age": 21, "grade": "B+"},
    "Kunal": {"age": 22, "grade": "A-"}
}
print("Students (Name, Grade):")
for name, details in students_nested.items():
    print(f"{name}: {details['grade']}")
print("-" * 40)

# 9. Loop Through a String
user_input = "Hello"
print("Characters in String:")
for char in user_input:
    print(char)
print("-" * 40)

# 10. Use enumerate() to Build a Menu
menu = ["Pizza", "Burger", "Pasta", "Salad"]
print("Menu:")
for index, item in enumerate(menu, start=1):
    print(f"{index}. {item}")

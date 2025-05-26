# Basic Python Concepts

This document summarizes foundational Python concepts with examples, covering everything from basic syntax to small projects. It's ideal for beginners looking to build a solid foundation in Python programming.

---

## 📌 Output and Strings

```python
print("Hello World")
```

**Multi-line output** using triple quotes:
```python
print("""Nature's first green is gold,
Her hardest hue to hold.
Her early leaf's a flower;
But only so an hour""")
```

**Custom separators and endings**:
```python
print("Hey", 6, 7, sep="~", end="\nUser")
```

---

## 📌 Variables and Data Types

```python
name = "John Doe"       # String
number = 1234567890     # Integer
is_active = True        # Boolean

print(f"My name is {name}, Number: {number}, Active: {is_active}")
print(type(name), type(number), type(is_active))
```

---

## 📌 Type Casting

```python
str_num1 = "45"
str_num2 = "234"
print(int(str_num1) + int(str_num2))
```

---

## 📌 Simple Calculator

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
```

---

## 📌 Advanced Calculator (With Operation Input)

```python
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
operation = input("Choose (Adn, Sbn, Dvn, Mlt): ")

if operation == "Adn":
    print(num1 + num2)
elif operation == "Sbn":
    print(num1 - num2)
elif operation == "Dvn":
    print("Error: Cannot divide by zero." if num2 == 0 else num1 / num2)
elif operation == "Mlt":
    print(num1 * num2)
else:
    print("Invalid operation.")
```

---

## 📌 String Manipulation

```python
name = "John Smith"
print(name[0])          # First character
print(len(name))        # String length
print(name.upper())     # Uppercase
print(name.lower())     # Lowercase
print(name.replace("John", "Jane"))  # Replace substring
print(name.split(" "))  # Split into words
print(name.capitalize())
print(name.center(50))
```

String method examples:

```python
sentence = "Python Programming is Fun"
print(sentence.find("is"))      # Index of "is"
print(sentence.endswith("Fun")) # Check ending
print(sentence.isalpha())       # All characters alphabetic
print(sentence.istitle())       # Title-case check
```

---

## 📌 Control Flow and Loops

**For loop example:**
```python
for i in range(0, 20, 5):
    print(i)
```

**While loop:**
```python
i = 1
while i <= 5:
    print("*" * i)
    i += 1
```

---

## 📌 Functions

```python
def average(a, b):
    return (a + b) / 2

print(average(10, 20))
```

---

## 📌 Lists and Tuples

```python
my_list = ["Alice", "Bob", "Charlie"]
my_list.append("David")
my_list.sort()
my_list.reverse()
my_list.insert(2, "Eve")
print(my_list)

tup = (1, 2, 3, 4, 5)
print(tup)
```

---

## 📌 Sets

```python
s = {1, 2, 3, 3, 4}
print(s)  # No duplicates

s1 = {1, 2}
s2 = {2, 3}
print(s1.union(s2))
print(s1.intersection(s2))
```

---

## 📌 Mini Projects

### ✅ Story Generator
```python
choice = input("Choose Option A or B: ").upper()
if choice == "A":
    print("You failed the test.")
elif choice == "B":
    print("You passed the test.")
```

### ✅ Time-Based Greeting
```python
import time
hour = int(time.strftime("%H"))
if hour < 12:
    print("Good Morning")
elif hour < 17:
    print("Good Afternoon")
else:
    print("Good Evening")
```

### ✅ Password Strength Checker
```python
import re

def pass_check(password):
    score = sum([
        len(password) >= 6,
        bool(re.search(r'\d', password)),
        bool(re.search(r'[A-Z]', password)),
        bool(re.search(r'[a-z]', password)),
        bool(re.search(r'[!@#$%^&*()]', password))
    ])
    return ["Invalid", "Weak", "Weak", "Medium", "Strong", "Strong"][score]

print(pass_check(input("Enter password: ")))
```

---

## 📌 Games

### 🎮 Guess the Number
```python
import random
secret = random.randint(1, 100)
guess = None
attempts = 0

while guess != secret:
    guess = int(input("Guess number: "))
    attempts += 1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")

print(f"Correct in {attempts} attempts!")
```

### 🕵️‍♂️ Secret Language Game

**Coding rule**:
- If word ≥ 3 chars: move first letter to end, add 3 random characters to both ends.
- If < 3: reverse it.

**Decoding reverses the above logic.**

---

## 📌 Recursion

**Factorial**
```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print(factorial(5))  # 120
```

**Fibonacci**
```python
def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))  # 5
```

---

## 📌 Text Analyzer

```python
text = input("Enter text: ")
print(len(text))              # Character count
print(len(text.split()))     # Word count
print(text.upper())
print(text.lower())
```



# Factorial Calculation
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(3))  # Output: 6
print(factorial(5))  # Output: 120
print(factorial(1))  # Output: 1

# Fibonacci Series
def fibonacci_series(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_series(n - 1) + fibonacci_series(n - 2)

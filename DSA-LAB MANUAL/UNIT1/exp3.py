def factorial(n):
    # Reject invalid input
    if n < 0:
        return "Invalid input! n must be >= 0"

    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)


# Input
n = int(input("Enter n: "))

# Output
result = factorial(n)
print("Factorial:", result) 
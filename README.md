# codealpha_task1
in this i upload code of my task 2 that is a basic chatbot in python.
def fibonacci_recursive(n):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Generate Fibonacci sequence up to a given number of terms
def generate_fibonacci_sequence(terms):
    return [fibonacci_recursive(i) for i in range(terms)]

# Example usage: Generate first 10 terms of the Fibonacci sequence
terms = 10
print(f"Fibonacci sequence with {terms} terms: {generate_fibonacci_sequence(terms)}")

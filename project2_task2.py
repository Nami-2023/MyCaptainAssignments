def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Example usage
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = fibonacci(n)
print("Fibonacci sequence for",n,"numbers: ",fib_sequence)
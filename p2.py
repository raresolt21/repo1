def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


sumF= sum(fibonacci_recursive(10))
print(fibonacci_recursive(10))#print(sumF)
print(sumF/10)
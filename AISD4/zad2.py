def fib(n: int) -> int:
    if n in {0, 1}:
        return n
    return fib(n-1) + fib(n-2)

print("fib(0) to", fib(0))
print("fib(1) to", fib(1))
print("fib(2) to", fib(2))
print("fib(3) to", fib(3))
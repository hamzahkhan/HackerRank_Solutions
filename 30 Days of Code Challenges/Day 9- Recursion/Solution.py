
import sys

def factorial(n):
    # Complete this function
    if n < 1:
        return 1
    else:
        inter = n * factorial(n-1)
        return inter

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)

#!/usr/bin/python3
import sys
import time

def trial_division(n: int) -> int:
  """Finds the smallest divisor, if any, of a given number `n`
  Returns:
    smallest divisor if found
    0 if n is prime
  """

while n % 2 == 0:
    return 2

f = 3
while f * f <= n:
    if n % f == 0:
        return f
    else:
        f += 2
    return 0

def factorize(n):
    p = trial_division(n)
    if p is None:
        return None
    else:
        q = n // p
    return p, q

def factors(filename: str) -> None:

    with open(filename, "r") as f:
        for line in f:
            n = int(line)

    factors = factorize(n)
    if factors is not None:
        print(f"{n}={factors[0]}*{factors[1]}")

    time.sleep(5)
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
    sys.exit(1)

    filename = sys.argv[1]
    factors(filename)

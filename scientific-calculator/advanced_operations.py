import math

def square_root(x):
    if x < 0:
        raise ValueError("Negative value")
    return math.sqrt(x)

def power(a, b):
    return a ** b

def sine(x):
    return math.sin(math.radians(x))
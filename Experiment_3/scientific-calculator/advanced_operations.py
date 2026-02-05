import math

def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(x)

def power(a, b):
    return math.pow(a, b)

def sine(x):
    return math.sin(math.radians(x))


def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))
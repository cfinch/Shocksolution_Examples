#!/usr/bin/env python

# From sequences to a sequence of tuples
a = range(0, 5)
b = range(5, 10)
c = range(10, 15)

sequence_of_tuples = zip(a, b, c)
print("Sequence of tuples:")
print(sequence_of_tuples)

# From a sequence of tuples to multiple sequences
a1, b1, c1 = zip(*sequence_of_tuples)
print("Separate sequences:")
print(a1)
print(b1)
print(c1)

# How it works
def test_fn(*args):
    """Number of arguments is not known in advance"""
    print("Arguments passed to function:")
    for a in args:
        print a

test_fn(*sequence_of_tuples)

# Convert tuples to lists (optional)
a1 = list(a1)
print(type(a1))

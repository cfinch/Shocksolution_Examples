#!/usr/bin/env python

import simple_example
import numpy as np

a = np.arange(0.0, 10.0, 1.0)
len_a = len(a)

print("foo:")
simple_example.test.foo(len_a)

print("bar:")
a_out = simple_example.test.bar(len_a, a)
print a_out

print("sub:")
a_out = simple_example.test.sub(a, len_a)
print(a_out)

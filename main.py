from random import random, uniform, expovariate
from math import exp

par1 = lambda: (random() - (x := random()) * x) < 0
par2 = lambda: random() - (x := random()) * x
nats = lambda: exp(random()) + 1
pi = lambda: 4 * (((x := random()) * x + (y := random()) * y) < 1)
montecarlo = lambda fx, n: sum((fx() for _ in range(n))) / n


def test(f):
    print(f.__name__, '\n')
    for _ in range(4):
        print(montecarlo(f, 100000))


# test(random)
# test(pi)
test(nats)
test(par1)
test(par2)
'''
for i in range(10):
  test(lambda: expovariate(float(i+1)))
'''

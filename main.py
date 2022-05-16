from random import random
from math import exp, fabs

nats = lambda : fabs(exp(random())) < 1
pi = lambda : 4*(((x := random())*x + (y := random())*y) < 1)
montecarlo = lambda fx, n : sum((fx() for _ in range(n)))/n

def test(f):
  for _ in range(10):
    print(montecarlo(f, 1000000))

test(random)
test(pi)
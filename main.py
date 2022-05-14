from random import random

dist = lambda : ((x := random())*x + (y := random())*y) < 1
montecarlo = lambda fx, n : sum((fx() for _ in range(n)))/n


for _ in range(10):
  print(montecarlo(random, 1000000))

for _ in range(10):
  print(4 * montecarlo(dist, 1000000))
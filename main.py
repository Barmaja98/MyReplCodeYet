from random import random

montecarlo = lambda n : sum((random() for _ in range(n)))/n

dist = lambda : ((x := random())*x + (y := random())*y) < 1
pi_est = lambda n : sum((dist() for _ in range(n)))/n


# for _ in range(10):
#   print(montecarlo(1000000))

for _ in range(10):
  print(4 * pi_est(1000000))
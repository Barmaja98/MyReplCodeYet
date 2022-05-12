from random import random

montecarlo = lambda n : sum((random() for _ in range(n)))/n

for _ in range(10):
  print(montecarlo(1000000))
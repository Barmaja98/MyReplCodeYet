from random import random

def montecarlo(n):
  return sum((random() for _ in range(n)))/n

for _ in range(10):
  print(montecarlo(1000000))
from random import random

def montecarlo(n):
  temp = (random() for _ in range(n)) 
  return sum(temp)/n

for _ in range(10):
  print(montecarlo(1000000))
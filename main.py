from random import random

def montecarlo(n):
  temp = 0
  for _ in range(n):
    temp += random()
  return temp/n

for _ in range(5):
  print(montecarlo(1000000))
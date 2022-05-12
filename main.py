from random import random

montecarlo = lambda n : sum((random() for _ in range(n)))/n

dist = int(random()^2 + random()^2 < 1)
pi_est = lambda n : sum((dist for _ in range(n))/n


# for _ in range(10):
#   print(montecarlo(1000000))

print(pi_est(100))
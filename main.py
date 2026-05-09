import math
import random

p = 1000
a = p

annRate = 10

variance = 20

years = 5

monAdd = 100
yearAdd = monAdd * 12

for i in range(years):
    rate = int(random.randint(annRate - variance, annRate + variance))

    a *= 1 + 0.01 * rate

    a += yearAdd
    print("Year ", i + 1, " amount: $", a)
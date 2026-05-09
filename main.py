import math
import random

p = 1000

annRate = 10

variance = 20

years = 5

monAdd = 100
yearAdd = monAdd * 12

prices = []

for j in range(1000): # monte carlo
    a = p
    for i in range(years): # calculate return
        rate = random.randint(annRate - variance, annRate + variance)
        a *= 1 + 0.01 * rate
        a += yearAdd
    prices.append(a) 


avg = sum(prices) / len(prices)

print("Avg price: $", avg)
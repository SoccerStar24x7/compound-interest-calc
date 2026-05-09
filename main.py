import math
import random

p = int(input("Principal: $"))

annRate = int(input("Annual Rate (ex. 10): "))

variance = int(input("Rate variance: "))

years = int(input("# of years: "))

monAdd = int(input("Monthly contribution: $"))
yearAdd = monAdd * 12

prices = [[]]

for j in range(1000): # monte carlo
    a = p
    for i in range(years): # calculate return
        rate = random.randint(annRate - variance, annRate + variance)
        a *= 1 + 0.01 * rate
        a += yearAdd
        try:
            prices[i].append(a)
        except IndexError:
            prices.append([])
            prices[i].append(a)
    

for i in range(len(prices)):
    print("Year", i + 1, "estimate: $", round(sum(prices[i])/len(prices[i]), 2))

# add matplotlib graphs? 
"""
import matplotlib as plt

plt.plot()
"""

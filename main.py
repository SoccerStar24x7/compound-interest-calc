import math
import random
import numpy as np
import csv
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
"""
p = int(input("Principal: $"))

annRate = int(input("Annual Rate (ex. 10): "))

variance = int(input("Rate variance: "))

years = int(input("# of years: "))
year = np.arange(years)


monAdd = int(input("Monthly contribution: $"))
"""
p = 1000
annRate = 10
variance = 20
years = 5 + 1
year = np.arange(years)

"""
for num in range(len(year)):
    year[num] += 1
"""

logging.debug(f"# of years: {len(year)}")

monAdd = 100
# sadf

yearAdd = monAdd * 12

prices = [[]]

for j in range(1000): # monte carlo
    a = p # every scenario reset
    for i in range(years): # for every year...
        if i == 0:
            continue
        rate = random.randint(annRate - variance, annRate + variance) # rate for that year
        a *= 1 + 0.01 * rate # applies the rate
        a += yearAdd # adds the monthly contribution
        a = round(a, 2)
        try:
            prices[i].append(a)
        except IndexError:
            prices.append([])
            prices[i].append(a)

prices[0] = [p]

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(prices) # Writes the entire 2D array at once

pr = []
for i in range(len(prices)):
    for j in range(len(prices[i])):
        pr.append(prices[i][j])
pr = np.array(pr)


# change years
ya = []
for x in range(len(prices)):
    for y in range(len(prices[x])):
        ya.append(x)

ya = np.array(ya)
logging.debug(f"len ya: {len(ya)}")
logging.debug(f"len pr: {len(pr)}")


avgs = []
for i in range(len(prices)):
    avg = round(sum(prices[i])/len(prices[i]), 2)
    avgs.append(avg)
    
for i in range(len(prices)):
    print("Year", i + 1, "estimate: $", avgs[i])

# add matplotlib graphs? 

logging.debug(f"len prices[0]: {len(prices[0])}")
logging.debug(f"len prices[1]: {len(prices[1])}")



import matplotlib.pyplot as plt

plt.scatter(year, avgs)

plt.title("Compound interest simulator")
plt.xlabel("Years") 
plt.ylabel("Price")

plt.minorticks_on()
plt.tick_params(labelright=True)
plt.tick_params(axis='y', which='both', right=True, labelright=True)

plt.show()
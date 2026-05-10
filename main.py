import math
import random
import numpy as np
import csv
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.getLogger('matplotlib.font_manager').disabled = True

logging.disable(logging.CRITICAL)

cycles = 1000

visualize = True

p = float(input("Principal: $"))

annRate = float(input("Annual Rate (ex. 10%): "))

variance = float(input("Rate variance (%): "))

years = int(input("# of years: ")) + 1
year = np.arange(years)

monAdd = float(input("Monthly contribution: $"))

yearAdd = monAdd * 12

prices = [[]]

for j in range(cycles): # monte carlo
    a = p # every scenario reset
    for i in range(years): # for every year...
        if i == 0:
            continue
        rate = random.randint(int(annRate - variance), int(annRate + variance)) # rate for that year
        a *= 1 + 0.01 * rate # applies the ratewd
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
    print(f"Year {i} estimate: ${avgs[i]}")


logging.debug(f"len prices[0]: {len(prices[0])}")
logging.debug(f"len prices[1]: {len(prices[1])}")


if not visualize:
    exit(0)

import matplotlib.pyplot as plt

logging.debug(f"len year: {len(year)}")
logging.debug(f"len pr: {len(pr)}")

# plt.scatter(ya, pr)

logging.debug(f"len prices[1]: {len(prices[1])}")

for i in range(len(prices[1])):
    b = []
    b.append(prices[0][0])
    for j in range(years):
        if j == 0:
            continue
        b.append(prices[j][i])
    
    plt.plot(year, b, linewidth=1, alpha=0.6)

plt.plot(year, avgs, linewidth=2.5, alpha=1)

plt.title("Compound interest sim.")
plt.xlabel("Years") 
plt.ylabel("Amount ($)")

plt.minorticks_on()
plt.tick_params(labelright=True)
plt.tick_params(axis='y', which='both', right=True, labelright=True)

plt.show()
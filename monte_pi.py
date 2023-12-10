import random

import matplotlib.pyplot as plt
from matplotlib import style

print(""" 
The Monte Carlo simulation is a mathematical technique that predicts possible outcomes of an uncertain event.
This method is used to understand the impact of risk and uncertainty.

Also known as the Multiple Probability Simulation, it is used in various fields such as 
Investing, Business, Sales, Physics, Engineering, etc. 

This technique was invented by John von Neumann and Stanislaw Ulam in the 1940s, named after a famous gambling location.
""")
# References
# https://aws.amazon.com/what-is/monte-carlo-simulation/#:~:text=The%20Monte%20Carlo%20simulation%20is,on%20a%20choice%20of%20action.
# https://www.investopedia.com/terms/m/montecarlosimulation.asp

style.use('dark_background')
points = 2000000
inside = 0

# Cordinates of points in & out of the circle for plotting
insidex = []
insidey = []
outsidex = []
outsidey = []

# Random points generating
for _ in range(points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    dist = x ** 2 + y ** 2  # Distance from origin

    if dist <= 1:
        inside += 1
        insidex.append(x)
        insidey.append(y)
    else:
        outsidex.append(x)
        outsidey.append(y)

# THEORY and approach for the simulation
# Square and a circle inscribed within it. r is radius of circle and 2r is side of square
r, pi = 1, 1  # draft values
area_sq = 4 * r * r  # side = 2r , area = 4r²
area_circle = pi * r * r  # radius = r, area = πr²
probability = (area_circle / area_sq)  # probability = πr²/4r² , π = 4 * probability

pie = 4 * (inside / points)  # probability = 4 * (points inside circle / total number of points within square)
print(f"Estimated value of π (pi) = {pie}")

# Creating the graph
plt.figure(figsize=(6, 6))
# LEGEND
# Sky Blue - Inside Circle; Light Coral - Outside Circle
plt.scatter(insidex, insidey, color='skyblue', label='Inside Circle')
plt.scatter(outsidex, outsidey, color='lightcoral', label='Outside Circle')
plt.title('Monte Carlo Simulation for π Estimation')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc='center')
plt.show()

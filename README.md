<div align="center">

# 🎯 Pi with Monte Carlo Simulations

Monte Carlo method — where randomness meets precision! Let's estimate the value of pi π in this unique method.

</div>

## 🎰 Description

The Monte Carlo simulation is a mathematical technique that predicts possible outcomes of an uncertain event.
It is a technique used to understand the impact of risk and uncertainty.

A Monte Carlo simulation is used to tackle a range of problems in many fields including investing, business, physics, and engineering. It is also referred to as a multiple probability simulation.

John von Neumann and Stanislaw Ulam invented the Monte Carlo simulation, or the Monte Carlo method, in the 1940s. They named it after the famous gambling location in Monaco because the method shares the same random characteristics as a roulette game.

## 🥧 Working
### Geometry Setup:
- Imagine a square with a side length $2r$ and a circle inscribed within it.
- This circle has a radius of $r$ and its area is $\[ A_{\text{circle}} = \pi r^2 \]$
- The area of the square is $\[ A_{\text{square}} = 4r^2 \]$

### Random Points:
- Randomly generate points within the square. 
- Each point is represented by coordinates $(x,y)$ where $x$ and $y$ are uniformly distributed random numbers between $−r$ and $r$.

### Calculations:
- Calculate the distance of each point from the origin $(0,0)$ using the formula $\[ d = \sqrt{x^2 + y^2} \]$
- Count the number of points that fall inside the circle $\(N_{\text{circle}}\)$, which corresponds to points where $\(x^2 + y^2 \leq r^2\)$.
- The number of points outside the circle $\(N_{\text{outside}}\)$ follow this condition $\(x^2 + y^2 > r^2\)$.

### Estimate π:
The ratio of points inside the circle to the total points generated is given by -

$\[ \frac{N_{\text{circle}}}{N_{\text{total}}} = \frac{A_{\text{circle}}}{A_{\text{square}}} = \frac{\pi r^2}{4r^2} = \frac{\pi}{4} \]$

Therefore, the estimated value of π is calculated as:

$\[ \pi \approx 4 \times \frac{N_{\text{circle}}}{N_{\text{total}}} \]$

## 🐐 Simulation
```
Estimated value of π (pi) = 3.140078
```
![Figure_2](https://github.com/ManjunathMGM/Monte-Carlo-pi/assets/84089882/5910d6c9-b96a-4cfb-ac03-2d0ffc1fadd4)

## 🤝 Contributing

Contributions are always welcome! Whether you find a bug, have a suggestion, or want to add a feature, just open an issue or submit a pull request. Let's improve this project together! ✨
</br>
> This project was undertaken as part of my coursework for MAT 205 - Mathematical Methods III: Statistics and Probability.

## :pencil: License

This project is licensed under [MIT](https://opensource.org/licenses/MIT) license.
</br>

## 😄 Author
> Manjunath MGM </br>

Shiv Nadar University </br>
mm153@snu.edu.in

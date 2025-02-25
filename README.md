# CS221 Final Project - [Hybrid Packing Algorithm: Optimizing Space Utilization and Suitcase Efficiency]

## Team Members

- [Gonzales, China Mae C.](https://github.com/chinagonzales)
- [Javier, April Kate M.](https://github.com/apriljavier)
- [Labay, Caryll L.](https://github.com/caryll-labay)

## Project Overview

In this project, we tackled the task of Optimizing Space Utilization and Suitcase Efficiency]. Our goal was to determine the minimum number of suitcases required to pack a given set of
 items, considering the size of each item and the capacity of the suitcases.

## File Structure

```
.
├── code
│ ├── main.py
│ └── ...
├── latex
│ ├── documentation.pdf
│ ├── presentation.pdf
│ └── ...
└── README.md

```

## How to Run the Project

To run our project, follow these steps :

1. Clone the repository to your local machine.
2. Install the necessary dependencies.
3. Navigate to the `code` directory.
4. Run the `main.py` script, which is the entry point of our project.

Make sure you have the required Python version and libraries installed before running the project.

## Summary of Findings

Our findings from the project indicate that the customized packing algorithm offers advantages in terms of simplicity, computational efficiency, and improved space utilization. By focusing solely on item size and eliminating weight considerations, the algorithm reduces computational overhead and provides a flexible solution for scenarios where weight differences are negligible. While it may not always yield the optimal number of suitcases, it achieves better packing efficiency compared to algorithms like Next Fit by distributing items more evenly.

We encountered challenges related to the algorithm's limitations when dealing with packing problems that involve significant weight disparities, fragile items, or specific stacking constraints. In such cases, the lack of weight consideration could lead to instability, and additional constraints would be required to ensure safe and efficient packing. Another challenge was optimizing space utilization further while maintaining computational efficiency.

Moving forward, it would be interesting to explore enhancements such as incorporating advanced optimization techniques like genetic algorithms, simulated annealing, or particle swarm optimization. Adding constraints for weight limitations, fragile item handling, and stacking restrictions would make the algorithm more versatile. Adaptive resizing techniques could dynamically adjust suitcase sizes based on item dimensions to minimize unused space. Furthermore, benchmarking against other algorithms and enabling real-time optimization in dynamic environments like e-commerce or production line packaging could provide deeper insights into its effectiveness and potential improvements.














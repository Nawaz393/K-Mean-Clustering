# Clustering Algorithm

[![License](https://img.shields.io/badge/license-Open%20Source-green.svg)](LICENSE)

## Description

This repository contains an implementation of a clustering algorithm that groups data points into clusters based on their proximity to a given number of centroid points (k).

## Table of Contents

- [Description](#description)
- [How it Works](#how-it-works)
- [How to Use](#how-to-use)
- [Example](#example)
- [Contributors](#contributors)
- [License](#license)

## How it Works

1. **Input Data:** The algorithm takes a set of data points as input. Each data point is represented by its coordinates (xo, yo).

2. **Choose K:** The user is prompted to enter the number of clusters (k) they want to create.

3. **Initialization:** The initial centroids (k points) are selected from the input data points.

4. **Clustering:** The algorithm iterates through each data point and assigns it to the nearest centroid based on the Euclidean distance.

5. **Update Centroids:** After assigning all data points to clusters, the centroids are recalculated by taking the average coordinates of the data points within each cluster.

6. **Repeat:** Steps 4 and 5 are repeated until the centroids no longer change significantly or a predefined number of iterations is reached.

7. **Output:** The algorithm returns the clusters formed, along with their respective centroid coordinates.

## How to Use

To use the clustering algorithm, follow these steps:

1. Clone the repository to your local machine.

2. Run the `test.py` file.

3. Enter the number of rows for your dataset.

4. For each row, input the coordinates (xo, yo) of the data points.

5. Enter the number of clusters (k) you want to create.

6. The program will display the resulting clusters set.

## Example

Suppose you have the following dataset:

| Data Point | xo | yo |
|------------|----|----|
|  1         | 3  | 4  |
|  2         | 7  | 5  |
|  3         | 2  | 8  |
|  4         | 1  | 2  |
|  5         | 6  | 3  |

Let's say you want to create 2 clusters (k=2).

Running the algorithm will yield the following result:

{K1=[1,3,4] K2=[2,5]}


## Contributors

This algorithm was developed by [Muhammad Nawaz khan] as a hobby project.
If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [Open Source License](LICENSE).

Happy clustering!



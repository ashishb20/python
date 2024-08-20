# Maze Solver with BFS and Curses

This project implements a maze-solving application using the Breadth-First Search (BFS) algorithm and a text-based user interface with the `curses` library. The application finds the shortest path from a start point to an end point in a given maze.

## Features

- **BFS Algorithm**: Efficiently finds the shortest path in the maze.
- **Text-Based UI**: Visualizes the maze and the pathfinding process using the `curses` library.
- **Dynamic Path Visualization**: Displays the step-by-step progress of the BFS algorithm with real-time updates.
- **Robust Maze Navigation**: Handles various maze configurations and edge cases.

## Requirements

- Python 3.x
- `curses` library (pre-installed with Python on Unix-based systems)


## Usage

1. Run the maze solver:
    ```sh
    python main.py
    ```

2. The application will display the maze and the pathfinding process. The start point is marked with `O` and the end point with `X`. The path will be highlighted in red.

## How It Works 
1. **Initialization**: The BFS algorithm starts from the start point (O) and initializes a queue with the start position and an empty path.
2. **Exploration**: The algorithm dequeues the front cell, marks it as visited, and explores its neighbors.
3. **Path Tracking**: For each neighbor, if it is not visited and not a wall, it is enqueued with the updated path
4. **Termination**: If the end point (X) is reached, the path is returned. If the queue is empty and the end point is not reached, there is no path.
## Example Maze

```python
maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "O", " ", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#", " ", "#"],
    ["#", "#", "#", "#", "#", "X", "#", "#", "#"]
]

# Treasure Placement Using CSP and Backtracking

## Overview

This project implements a treasure placement system in an 8×8 grid environment using **Constraint Satisfaction Problem (CSP)** modeling and the **Backtracking algorithm**.

The environment consists of free cells, bricks (obstacles), pits, and treasures. The main objective is to place all treasures in valid locations while ensuring that each treasure is reachable from the starting position.

This implementation covers tasks **14 and 15** of the project.

## Implemented Tasks

### Task 14 – CSP Modeling

The treasure placement problem is modeled as a Constraint Satisfaction Problem (CSP).

- **Variables:** The locations of the treasures.
- **Domains:** All available free cells in the grid, excluding the starting position.
- **Constraints:**
  - A treasure cannot be placed on a brick or a pit.
  - Multiple treasures cannot occupy the same cell.
  - Every treasure must be reachable from the starting position.

### Task 15 – Backtracking

A recursive Backtracking algorithm is implemented to find a valid assignment for all treasures.

The algorithm works as follows:

1. Collect all available free cells and create the domain.
2. Randomize the order of candidate cells.
3. Select a candidate cell.
4. Check whether the cell is reachable from the starting position using BFS.
5. Add the cell to the current assignment if it satisfies the constraints.
6. Recursively continue until all treasures are placed.
7. If a valid assignment cannot be found, backtrack and try another candidate.

The implementation uses randomized candidate ordering rather than the MRV heuristic.

## Environment Configuration

The grid has 8 rows and 8 columns (64 cells).

Three difficulty levels are available:

| Level | Bricks | Pits | Treasures |
|---|---:|---:|---:|
| Easy | 5 | 0 | 2 |
| Medium | 8 | 2 | 3 |
| Hard | 12 | 4 | 5 |

The starting position is cell index `0` (top-left corner).

Brick and pit locations are generated randomly.

## Algorithms and Data Structures

- **Backtracking:** Recursive search for a valid treasure placement.
- **Breadth-First Search (BFS):** Checks whether a candidate cell is reachable from the starting position.
- **Queue:** Used in BFS to explore neighboring cells.
- **Set:** Used to keep track of visited cells.
- **List:** Used to store the grid, candidate domains, and current assignments.

## Project Structure

```text
project/
│
├── main.py       # Grid, Square, and treasure placement algorithms
├── test.py       # Tests different difficulty levels and methods
└── README.md
```

## Requirements

- Python 3.x
- No external libraries are required.

The project uses Python's built-in modules:

- `collections`
- `random`

## How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd <project-directory>
```

Run the test file:

```bash
python test.py
```

The test script runs the program with three difficulty levels using both random placement and Backtracking.

## Example Output

The grid is displayed using the following symbols:

| Symbol | Meaning |
|---|---|
| ` ` | Free cell |
| `B` | Brick |
| `P` | Pit |
| `T` | Treasure |

Example:

```text
  | B |   |   | T |   |   |   |
  |   | P |   | B |   |   |   |
T |   |   | B |   |   |   |   |
  |   |   |   |   | P |   |   |
  | B |   |   |   |   |   |   |
  |   |   | T |   |   |   |   |
  |   |   |   | B |   |   |   |
  |   |   |   |   |   |   |   |
```

*Note: The actual output is randomly generated and will be different each time.*

## Author

Implemented as part of the Artificial Intelligence course project, covering CSP modeling and Backtracking search (Tasks 14 and 15).

# Sliding number puzzle solver
This serves as a solver for the classic Sliding Number Puzzle in 3x3 grid using numbers 1 – 8. 
The original goal of the game is to sort numbers from 1 to 8 with the last cell remaining empty. However, this algorithm is capable of finding a solution path between any two valid game states.

You can solve the puzzle using either the Depth-First search or the A* algorithm. The application is easily extendable to larger grids with more numbers.

## Technologies
* **Programming language**: Python 3.11.9
* **Framework**: Tkinter (for graphical visualisation of a algorithm tree)

## Algorithms
Find the path from the original to the goal game state, you can use one of the following algorithms:

* **Depth-First search**
    call: depth_first_search(state, tree, visites)
* **A\* algorithm**
    call: a_star_search(state, tree)
  
In the A\* you can also customize the  **heurstic cost** calculation by modifying the method set_heuristic_cost(state, goal) inside State class.

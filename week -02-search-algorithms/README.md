# Week 02: Search Algorithms - Workshop README

## 1. High-Level Overview

Welcome to the **Week 02: Search Algorithms** university coursework workshop folder. This module focuses on foundational and informed graph search algorithms in Artificial Intelligence. 

Graph search algorithms are core building blocks for navigation, puzzle-solving, game AI, and routing. In this workshop, we implement and analyze both **uninformed (blind) search strategies**—which explore graphs without information about the goal's location—and **informed (heuristic) search strategies**—which leverage domain-specific heuristics to guide the search more efficiently toward the goal.

The provided Python script (`workshop2-algorithms.py`) models various data structures (trees, directed graphs, weighted graphs, and regional maps) and implements foundational pathfinding algorithms from scratch using standard Python libraries.

---

## 2. Detailed File and Function Breakdown

The primary code file in this repository is `workshop2-algorithms.py`. Below is an exhaustive breakdown of every data structure, function, task runner, and programming concept utilized within it.

### A. Graph Data Structures
The script defines multiple graph representations using Python dictionaries, mapping node keys to lists of neighboring nodes (or tuples of neighboring nodes and edge weights):
* **`graph_tree`**: A standard hierarchical tree layout used for basic BFS and DFS testing.
* **`graph_ah`**: A directed graph containing nodes from 'A' to 'H' with specific directional edges.
* **`graph_weighted_tree`**: A tree where edges have explicit numerical costs, represented as tuples `(neighbor, cost)`.
* **`graph_weighted_ah`**: A weighted directed graph spanning nodes 'A' to 'H'.
* **`maze_1` & `maze_sunderland`**: Undirected graphs representing grid-like mazes and real-world regional transport links (e.g., Newcastle, Sunderland, Durham).
* **`graph_greedy` & `graph_astar`**: Specialized graphs coupled with a `heuristic` dictionary containing estimated costs from each node to the goal.

---

### B. Core Search Algorithms & Functions

#### 1. Breadth-First Search (`bfs`)
* **Purpose**: Explores the graph level-by-level, guaranteeing the shortest path in unweighted graphs.
* **Inputs**: `graph` (dict), `start` (str), `goal` (str), `show_steps` (bool).
* **Outputs**: Returns the list representing the path from start to goal, or `None` if unreachable.
* **Algorithm & Logic**: 
  * Utilizes a First-In, First-Out (FIFO) queue initialized with `(start, [path])`.
  * Dequeues the front node, checks if it is the goal, and if not, appends all unvisited neighbors along with the updated tracking path to the queue.
* **Concepts Used**: FIFO queues (`list.pop(0)`), path reconstruction via list concatenation, state tracking (`visited` list).

#### 2. Depth-First Search (`dfs`)
* **Purpose**: Explores as deep as possible along each branch before backtracking. Does not guarantee the shortest path.
* **Inputs**: `graph` (dict), `start` (str), `goal` (str), `show_steps` (bool).
* **Outputs**: Returns the path list, or `None`.
* **Algorithm & Logic**: 
  * Utilizes a Last-In, First-Out (LIFO) stack initialized with `(start, [path])`.
  * Pops the last node from the stack. To maintain expected left-to-right traversal order when pushing to a stack, neighbors are pushed in **reversed** order (`reversed(graph.get(node, []))`).
* **Concepts Used**: LIFO stacks (`stack.pop()`), sequence reversal, tree/graph traversal.

#### 3. Uniform Cost Search (`ucs`)
* **Purpose**: Finds the least-cost path in weighted graphs. Equivalent to Dijkstra's algorithm.
* **Inputs**: `graph` (dict with edge weights), `start` (str), `goal` (str).
* **Outputs**: Returns a tuple `(path_list, total_cost)`.
* **Algorithm & Logic**: 
  * Uses a priority queue (`heapq`) ordered by accumulated path cost `(cost, node, path)`.
  * At each step, the node with the lowest cumulative cost is expanded. Edge weights are added to the running cost as new nodes are pushed.
* **Concepts Used**: Priority queues (`heapq.heappush`, `heapq.heappop`), cost accumulation, optimal path finding.

#### 4. Greedy Best-First Search (`greedy_best_first_search`)
* **Purpose**: An informed search algorithm that expands the node closest to the goal, as estimated by a heuristic function $h(n)$.
* **Inputs**: `graph` (dict), `start` (str), `goal` (str), `heuristic` (dict).
* **Outputs**: Returns the visited traversal path list.
* **Algorithm & Logic**: 
  * Uses a `PriorityQueue` storing elements prioritized strictly by their heuristic value: `(heuristic_value, node)`.
  * Greedily picks nodes that look closest to the target according to $h(n)$, ignoring actual path costs incurred so far.
* **Concepts Used**: Heuristics, Informed Search, `queue.PriorityQueue`.

#### 5. A* Search (`a_star_search`)
* **Purpose**: Combines UCS and Greedy Search by evaluating nodes using $f(n) = g(n) + h(n)$, where $g(n)$ is the exact cost from the start node and $h(n)$ is the heuristic estimated cost to the goal. Guaranteed to find the shortest path if $h(n)$ is admissible.
* **Inputs**: `graph` (dict), `start` (str), `goal` (str), `heuristic` (dict).
* **Outputs**: Returns the reconstructed optimal path list.
* **Algorithm & Logic**: 
  * Maintains a priority queue of `(f_cost, node)`, a `g_costs` tracking dictionary for exact path costs, and a `came_from` dictionary for backtracking.
  * Dynamically updates costs if a cheaper path to an already-seen node is discovered.
* **Concepts Used**: Evaluation function $f(n) = g(n) + h(n)$, admissibility, path reconstruction helper functions.

#### 6. Helper Functions
* **`reconstruct_path(came_from, start, goal)`**: Backtracks from the goal node to the start node using the `came_from` mapping dictionary and reverses it to output a clean chronological path string.
* **`reverse_graph_greedy(graph)`**: Flips directed edges in a graph structure for reverse-search testing scenarios.

---

### C. Task Runners
The file provides modular execution functions (`run_task_1()`, `run_task_2()`, `run_task_3()`) which execute specific search configurations, measure precise code performance using `time.perf_counter()`, and print formatted diagnostic readouts to the console.

---

## 3. How to Run the Script

Ensure you have **Python 3.6 or higher** installed on your system. No external package installations (like pip dependencies) are required since all imports (`time`, `heapq`, `queue`) are part of the Python Standard Library.

1. Open your terminal or command prompt.
2. Navigate to the folder containing the script:
   ```bash
   cd path/to/week-02-search-algorithms
   ```
3. Execute the script using Python:
   ```bash
   python workshop2-algorithms.py
   ```

import time
import heapq
from queue import PriorityQueue

# Task 1 & 2: Basic Tree Graph[cite: 9]
graph_tree = {
    'A': ['B', 'E'],
    'B': ['C', 'D'],
    'C': [],
    'D': [],
    'E': ['F', 'G'],
    'F': [],
    'G': []
}

# Task 1c & 2a: Directed Graph A-H[cite: 10]
graph_ah = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['E', 'H'],
    'G': ['H'],
    'H': []
}

# Task 3: Weighted Tree[cite: 12]
graph_weighted_tree = {
    'A': [('B', 1), ('E', 2)],
    'B': [('D', 3), ('C', 4)],
    'C': [],
    'D': [],
    'E': [('F', 3), ('G', 2)],
    'F': [],
    'G': []
}

# Task 3b: Weighted Graph A-H[cite: 12]
graph_weighted_ah = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 3)],
    'D': [('G', 2)],
    'E': [],
    'F': [('E', 2), ('H', 4)],
    'G': [('H', 1)],
    'H': []
}

# Task 4a: Simple Maze (Undirected to allow bidirectional travel)[cite: 12]
maze_1 = {
    'A': ['B'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'F'],
    'D': ['G'],
    'E': ['B', 'F', 'H'],
    'F': ['C', 'E', 'I'],
    'G': ['D', 'H'],
    'H': ['E', 'G'],
    'I': ['F']
}

# Task 4c: Sunderland Regional Map (Undirected)
maze_sunderland = {
    'Newcastle': ['South Shields', 'Sunderland', 'Chester-le-Street'],
    'South Shields': ['Newcastle', 'Sunderland'],
    'Sunderland': ['Newcastle', 'South Shields', 'Seaham', 'Durham'],
    'Seaham': ['Sunderland', 'Durham'],
    'Chester-le-Street': ['Newcastle', 'Durham'],
    'Durham': ['Sunderland', 'Seaham', 'Chester-le-Street']
}

# Task 5: Greedy Best-First Search Graph & Heuristics[cite: 14]
graph_greedy = {
    'A': [('B', 0), ('E', 0)],
    'B': [('C', 0), ('D', 0)],
    'C': [],
    'D': [],
    'E': [('F', 0), ('G', 0)],
    'F': [],
    'G': []
}

heuristic = {
    'A': 7, 'B': 6, 'C': 2, 'D': 6, 'E': 1, 'F': 3, 'G': 0
}

# Task 6: A* Search Graph (Updated Costs)[cite: 15]
graph_astar = {
    'A': [('B', 3), ('E', 5)],
    'B': [('C', 2), ('D', 4)],
    'C': [],
    'D': [],
    'E': [('F', 3), ('G', 1)],
    'F': [],
    'G': []
}

# Task 1: Breadth-First Search[cite: 9]
def bfs(graph, start, goal, show_steps=True):
    visited = []
    queue = [(start, [])]
    while queue:
        node, path = queue.pop(0)
        if show_steps:
            print(f"Current node: {node}, Path: {path + [node]}")
        if node == goal:
            return path + [node]
        if node not in visited:
            visited.append(node)
            for neighbour in graph.get(node, []):
                queue.append((neighbour, path + [node]))
    if show_steps:
        print("Goal not found")
    return None

# Task 2: Depth-First Search[cite: 11]
def dfs(graph, start, goal, show_steps=True):
    visited = []
    stack = [(start, [])]
    while stack:
        node, path = stack.pop()
        if show_steps:
            print(f"Current node: {node}, Path: {path + [node]}")
        if node == goal:
            return path + [node]
        if node not in visited:
            visited.append(node)
            for neighbour in reversed(graph.get(node, [])):
                stack.append((neighbour, path + [node]))
    if show_steps:
        print("Goal not found")
    return None

# Task 3: Uniform Cost Search[cite: 11]
def ucs(graph, start, goal):
    visited = []
    priority_queue = [(0, start, [])]
    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        print(f"Current node: {node}, Path: {path + [node]}, Cost: {cost}")
        if node == goal:
            return path + [node], cost
        if node not in visited:
            visited.append(node)
            for neighbour, edge_cost in graph.get(node, []):
                if neighbour not in visited:
                    new_cost = cost + edge_cost
                    heapq.heappush(priority_queue, (new_cost, neighbour, path + [node]))
    print("Goal not found")
    return None, 0

# Task 5: Greedy Best-First Search[cite: 14]
def greedy_best_first_search(graph, start, goal, heuristic):
    open_list = PriorityQueue()
    open_list.put((heuristic.get(start, float('inf')), start))
    visited = set()
    path = []
    
    print("Greedy Best-First Search Path:")
    while not open_list.empty():
        current_heuristic, current = open_list.get()
        path.append(current)
        print(f"{current} ", end="")
        if current == goal:
            print("\nGoal reached!")
            return path
        visited.add(current)
        for neighbor, _ in graph.get(current, []):
            if neighbor not in visited:
                open_list.put((heuristic.get(neighbor, float('inf')), neighbor))
    print("\nGoal not reachable.")
    return None

# Task 6: A* Search[cite: 15]
def a_star_search(graph, start, goal, heuristic):
    open_list = PriorityQueue()
    open_list.put((0 + heuristic.get(start, float('inf')), start))
    g_costs = {start: 0}
    came_from = {}
    visited = set()

    while not open_list.empty():
        f, current = open_list.get()
        print(f"Visiting: {current} (f={f}, g={g_costs[current]}, h={heuristic.get(current, float('inf'))})")
        if current == goal:
            print("Goal reached!")
            return reconstruct_path(came_from, start, goal)
        
        visited.add(current)
        for neighbor, cost in graph.get(current, []):
            tentative_g = g_costs[current] + cost
            if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g
                f_cost = tentative_g + heuristic.get(neighbor, float('inf'))
                open_list.put((f_cost, neighbor))
                came_from[neighbor] = current
    print("Goal not reachable.")
    return None

def reconstruct_path(came_from, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    print("Path found:", " -> ".join(path))
    return path

# Helper to reverse graphs for backwards searches (Tasks 5b/c, 6c/d)
def reverse_graph_greedy(graph):
    reversed_g = {k: [] for k in graph.keys()}
    for node, edges in graph.items():
        for edge, cost in edges:
            reversed_g[edge].append((node, cost))
    return reversed_g


# ==========================================
# TASK RUNNERS
# ==========================================

def run_task_1():
    print("\n--- Task 1a & 1b: BFS on Tree (With Execution Time) ---")
    tests = [('A', 'E'), ('B', 'G'), ('A', 'G')]
    for start, goal in tests:
        print(f"\nSearching from {start} to {goal}:")
        start_time = time.perf_counter()
        result = bfs(graph_tree, start, goal)
        end_time = time.perf_counter()
        if result:
            print(f"Path found: {result}")
        print(f"Execution time: {(end_time - start_time) * 1000:.4f} ms")

    print("\n--- Task 1c & 1d: BFS on Graph A-H ---")
    result = bfs(graph_ah, 'A', 'H')
    if result:
        print(f"Path found from A to H: {result}")

def run_task_2():
    print("\n--- Task 2a: DFS on Tree (With Execution Time) ---")
    tests = [('A', 'E'), ('B', 'G'), ('A', 'G')]
    for start, goal in tests:
        print(f"\nSearching from {start} to {goal}:")
        start_time = time.perf_counter()
        result = dfs(graph_tree, start, goal)
        end_time = time.perf_counter()
        if result:
            print(f"Path found: {result}")
        print(f"Execution time: {(end_time - start_time) * 1000:.4f} ms")

    print("\n--- DFS on Graph A-H ---")
    result = dfs(graph_ah, 'A', 'H')
    if result:
        print(f"Path found from A to H: {result}")

def run_task_3():
    print("\n--- Task 3a: UCS on Weighted Tree (A to F) ---")
    path, cost = ucs(graph_weighted_tree, 'A', 'F')
    print(f"Optimal Path found: {path} with total cost: {cost}")

    print("\n--- Task 3c: UCS on Weighted Graph A-H (A to E) ---")
    path, cost = ucs(graph_weighted_ah, 'A', 'E')
    print(f"Optimal Path found: {path} with total cost: {cost}")

def run_task_4():
    print("\n--- Task 4b: Solve Maze (C to G) ---")
    print("BFS:")
    bfs(maze_1, 'C', 'G', show_steps=False)
    print("DFS:")
    dfs(maze_1, 'C', 'G', show_steps=False)

    print("\n--- Task 4c: Sunderland Regional Map (Sunderland to all) ---")
    locations = ['Newcastle', 'South Shields', 'Seaham', 'Chester-le-Street', 'Durham']
    for loc in locations:
        print(f"\nBFS from Sunderland to {loc}:")
        path = bfs(maze_sunderland, 'Sunderland', loc, show_steps=False)
        print(f"Path: {path}")

def run_task_5():
    print("\n--- Task 5a: Greedy Best-First (A to F) ---")
    # F is unreachable in a greedy graph due to heuristic trap if F=3 and E=1
    greedy_best_first_search(graph_greedy, 'A', 'F', heuristic)

    print("\n--- Task 5b & 5c: Greedy Best-First Backwards ---")
    rev_graph = reverse_graph_greedy(graph_greedy)
    print("\nG to A:")
    greedy_best_first_search(rev_graph, 'G', 'A', heuristic)
    print("\nG to C:")
    greedy_best_first_search(rev_graph, 'G', 'C', heuristic)

def run_task_6():
    print("\n--- Task 6a: A* Search (A to G) ---")
    a_star_search(graph_astar, 'A', 'G', heuristic)

    print("\n--- Task 6b: A* Search (A to F) ---")
    a_star_search(graph_astar, 'A', 'F', heuristic)

    print("\n--- Task 6c & 6d: A* Search Backwards ---")
    rev_astar = reverse_graph_greedy(graph_astar)
    print("\nG to A:")
    a_star_search(rev_astar, 'G', 'A', heuristic)
    print("\nG to C:")
    a_star_search(rev_astar, 'G', 'C', heuristic)

# ==========================================
# MENU SYSTEM
# ==========================================

def main():
    tasks = {
        "1": ("Task 1: Breadth-First Search (BFS)", run_task_1),
        "2": ("Task 2: Depth-First Search (DFS)", run_task_2),
        "3": ("Task 3: Uniform Cost Search (UCS)", run_task_3),
        "4": ("Task 4: Maze Solving", run_task_4),
        "5": ("Task 5: Greedy Best-First Search", run_task_5),
        "6": ("Task 6: A* Search", run_task_6)
    }

    while True:
        print("\n" + "="*35)
        print(" DTS301 Workshop 2: Search Menu ")
        print("="*35)
        for key, (desc, _) in tasks.items():
            print(f"[{key}] {desc}")
        print("[q] Quit")

        choice = input("\nSelect a task to run: ").strip().lower()

        if choice == "q":
            break
        elif choice in tasks:
            print(f"\n=== Running {tasks[choice][0]} ===")
            tasks[choice][1]()
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()
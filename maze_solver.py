import heapq

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        r, c = current
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            neighbor = (r+dr, c+dc)
            nr, nc = neighbor
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != 1:
                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found

def print_maze(maze, path=None):
    symbols = {0: '.', 1: '#'}
    path_set = set(path) if path else set()
    for r, row in enumerate(maze):
        line = ''
        for c, cell in enumerate(row):
            pos = (r, c)
            if pos == start:   line += 'S'
            elif pos == goal:  line += 'G'
            elif pos in path_set: line += '*'
            else: line += symbols[cell]
        print(line)

# Example usage
maze = [
    [0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

start = (0, 0)
goal  = (4, 6)

path = astar(maze, start, goal)

if path:
    print(f"Path found! Length: {len(path)} steps")
    print_maze(maze, path)
else:
    print("No path exists — goal is unreachable.")
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    open_list = [start]
    closed_list = []

    g = {}
    g[start] = 0

    parent = {}

    while open_list:
        current = open_list[0]

        # find node with lowest f
        for node in open_list:
            if g[node] + heuristic(node, goal) < g[current] + heuristic(current, goal):
                current = node

        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path

        open_list.remove(current)
        closed_list.append(current)

        for move in [(0,1),(0,-1),(1,0),(-1,0)]:
            neighbor = (current[0] + move[0], current[1] + move[1])

            if neighbor[0] < 0 or neighbor[1] < 0 or \
               neighbor[0] >= len(grid) or neighbor[1] >= len(grid[0]):
                continue

            if grid[neighbor[0]][neighbor[1]] == 1:
                continue

            if neighbor in closed_list:
                continue

            temp_g = g[current] + 1

            if neighbor not in open_list:
                open_list.append(neighbor)
            elif temp_g >= g.get(neighbor, 999):
                continue

            parent[neighbor] = current
            g[neighbor] = temp_g

    return "No Path Found"
print(A* algorithm)


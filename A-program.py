import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    open_list = []
    heapq.heappush(open_list, (0, start))

    g = {start: 0}
    parent = {}

    closed_set = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path

        closed_set.add(current)

        for move in [(0,1),(0,-1),(1,0),(-1,0)]:
            neighbor = (current[0] + move[0], current[1] + move[1])

            if (0 <= neighbor[0] < rows and 
                0 <= neighbor[1] < cols and 
                grid[neighbor[0]][neighbor[1]] == 0):

                if neighbor in closed_set:
                    continue

                temp_g = g[current] + 1

                if neighbor not in g or temp_g < g[neighbor]:
                    g[neighbor] = temp_g
                    f = temp_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f, neighbor))
                    parent[neighbor] = current

    return "No Path Found"


# ---------------- RUN PROGRAM ----------------

grid = [
    [0,0,0,0],
    [1,1,0,1],
    [0,0,0,0],
    [0,1,1,0]
]

start = (0,0)
goal = (3,3)

result = astar(grid, start, goal)
print("Path:", result)




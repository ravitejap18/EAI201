from collections import defaultdict, deque
import heapq
import math

# Junction coordinates.
nodes = {
    'A': (0, 0),
    'B': (3, 4),
    'C': (8, 2),
    'D': (5, 8),
    'E': (10, 6),
}

# Pipes with weights.
edges = [
    ('A','B',5),
    ('A','C',10),
    ('B','C',3),
    ('B','D',7),
    ('C','E',4),
    ('D','E',2),
]

# Build graph
def make_graph(edges):
    g = defaultdict(list)
    for n1, n2, w in edges:
        g[n1].append((n2, w))
        g[n2].append((n1, w))
    return g

graph = make_graph(edges)

# Calculate path cost.
def get_cost(graph, path):
    total = 0
    for i in range(len(path)-1):
        a, b = path[i], path[i+1]
        for neigh, w in graph[a]:
            if neigh == b:
                total += w
                break
    return total

# Depth- First Search
def dfs(graph, start, end):
    visited = set()
    final_path = []
    nodes_seen = 0

    def search(node, path):
        nonlocal final_path, nodes_seen
        visited.add(node)
        nodes_seen += 1
        path.append(node)

        if node == end:
            final_path = path.copy()
            return True

        for neigh, _ in sorted(graph[node], key=lambda x: x[0]):
            if neigh not in visited and search(neigh, path):
                return True

        path.pop()
        return False

    search(start, [])
    return final_path, get_cost(graph, final_path), nodes_seen

# Breadth-First Search
def bfs(graph, start, end):
    queue = deque([(start, [start])])
    visited = {start}
    nodes_seen = 0

    while queue:
        current, path = queue.popleft()
        nodes_seen += 1
        if current == end:
            return path, get_cost(graph, path), nodes_seen
        for neigh, _ in sorted(graph[current], key=lambda x: x[0]):
            if neigh not in visited:
                visited.add(neigh)
                queue.append((neigh, path + [neigh]))
    return [], 0, nodes_seen

# Dijkstra's algorithm
def dijkstra(graph, start, end):
    dist = {n: float('inf') for n in graph}
    dist[start] = 0
    prev = {}
    heap = [(0, start)]
    visited_nodes = set()
    nodes_seen = 0

    while heap:
        d, node = heapq.heappop(heap)
        if node in visited_nodes:
            continue
        visited_nodes.add(node)
        nodes_seen += 1
        if node == end:
            break
        for neigh, w in graph[node]:
            new_dist = d + w
            if new_dist < dist.get(neigh, float('inf')):
                dist[neigh] = new_dist
                prev[neigh] = node
                heapq.heappush(heap, (new_dist, neigh))

    path = []
    n = end
    while n in prev or n == start:
        path.append(n)
        if n == start:
            break
        n = prev[n]
    path.reverse()
    return path, dist.get(end, float('inf')), nodes_seen

# A* heuristic
def heuristic(a, b):
    x1, y1 = nodes[a]
    x2, y2 = nodes[b]
    return math.hypot(x2 - x1, y2 - y1)

# A* search
def astar(graph, start, end):
    open_list = [(heuristic(start, end), start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    nodes_seen = 0

    while open_list:
        _, current = heapq.heappop(open_list)
        nodes_seen += 1
        if current == end:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, g_score[end], nodes_seen

        for neigh, w in graph[current]:
            tentative = g_score[current] + w
            if tentative < g_score.get(neigh, float('inf')):
                came_from[neigh] = current
                g_score[neigh] = tentative
                f_score[neigh] = tentative + heuristic(neigh, end)
                heapq.heappush(open_list, (f_score[neigh], neigh))

    return [], 0, nodes_seen

# Run algorithms
graph = make_graph(edges)

dfs_path, dfs_cost, dfs_seen   = dfs(graph, 'A', 'E')
bfs_path, bfs_cost, bfs_seen   = bfs(graph, 'A', 'E')
dij_path, dij_cost, dij_seen   = dijkstra(graph, 'A', 'E')
a_path, a_cost, a_seen         = astar(graph, 'A', 'E')

print("DFS      : ", dfs_path, "|| cost =", dfs_cost, "|| visited =", dfs_seen)
print("BFS      : ", bfs_path, "|| cost =", bfs_cost, "|| visited =", bfs_seen)
print("Dijkstra : ", dij_path, "|| cost =", dij_cost, "|| visited =", dij_seen)
print("A*       : ", a_path,  "|| cost =", a_cost,  "|| visited =", a_seen)

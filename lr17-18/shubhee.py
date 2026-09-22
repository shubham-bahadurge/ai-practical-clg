# A* Algorithm

def aStarAlgo(start_node, stop_node):

    open_set = set(start_node)
    closed_set = set()

    g = {}              # Distance from starting node
    parents = {}        # Parent of each node

    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:

        n = None

        # Find node with lowest f(n) = g(n) + h(n)
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        # If goal node is reached
        if n == stop_node:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)
            path.reverse()

            print("Path found: {}".format(path))
            return path

        # If node has no neighbours
        if Graph_nodes[n] is None:
            pass

        else:
            # Check all neighbours
            for (m, weight) in get_neighbors(n):

                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    # Check whether new path is shorter
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        # If node is in closed set,
                        # remove it and add to open set
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n is None:
            print("Path does not exist!")
            return None

        # Move current node from open to closed
        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist!")
    return None


# Function to return neighbours and their distances
def get_neighbors(v):

    if v in Graph_nodes:
        return Graph_nodes[v]

    else:
        return None


# Heuristic function
def heuristic(n):

    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0
    }

    return H_dist[n]


# Define the graph
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
    'G': []
}


# Run A* Algorithm
aStarAlgo('A', 'G')

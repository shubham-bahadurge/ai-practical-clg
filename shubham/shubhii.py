from collections import deque

# MazeProblem class defines the maze structure and movement rules
class MazeProblem:
    def __init__(self, maze):
        self.maze = maze
        self.start, self.goal = self.find_positions()

    def find_positions(self):
        start = goal = None

        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 'S':
                    start = (i, j)
                elif self.maze[i][j] == 'G':
                    goal = (i, j)

        return start, goal

    def get_successors(self, state):
        successors = []

        # Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            x, y = state[0] + dx, state[1] + dy

            if 0 <= x < len(self.maze) and 0 <= y < len(self.maze[0]):
                if self.maze[x][y] != 1:  # 1 is a wall
                    successors.append((x, y))

        return successors


# Breadth-First Search (BFS) implementation
def bfs(problem):
    frontier = deque()

    frontier.append((problem.start, [problem.start]))
    explored = set()

    while frontier:
        state, path = frontier.popleft()

        if state == problem.goal:
            return path

        if state not in explored:
            explored.add(state)

            for neighbor in problem.get_successors(state):
                if neighbor not in explored:
                    frontier.append((neighbor, path + [neighbor]))

    return None


# Depth-First Search (DFS) implementation
def dfs(problem):
    frontier = [(problem.start, [problem.start])]
    explored = set()

    while frontier:
        state, path = frontier.pop()

        if state == problem.goal:
            return path

        if state not in explored:
            explored.add(state)

            for neighbor in problem.get_successors(state):
                if neighbor not in explored:
                    frontier.append((neighbor, path + [neighbor]))

    return None


# Sample maze grid
# S = Start, G = Goal, 0 = open, 1 = wall

maze = [
    ['S', 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 'G']
]


# Create problem instance
problem = MazeProblem(maze)


# Solve using BFS and DFS
bfs_path = bfs(problem)
dfs_path = dfs(problem)


# Print results
print("BFS Path from 'S' to 'G':")
print(bfs_path)

print("\nDFS Path from 'S' to 'G':")
print(dfs_path)
import tkinter as tk
import time
import heapq

# ================= MAZE =================
maze = [
    [0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],
    [1,1,0,1,0,1,1,0,1,0,1,1,1,1,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,0,1,1,1,1,1,1,0,1,0],
    [0,0,0,0,1,0,0,0,0,0,0,1,0,0,0],
    [1,1,1,0,1,1,1,1,1,1,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,0,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],
    [1,1,1,1,1,1,0,1,1,1,1,1,0,1,0],
    [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0],
    [0,1,1,1,0,1,1,1,1,1,0,1,1,1,0],
    [0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

ROWS = len(maze)
COLS = len(maze[0])
START = (0, 0)
GOAL = (ROWS - 1, COLS - 1)
CELL = 35

# ================= GUI =================
root = tk.Tk()
root.title("Best First Search Maze Solver")
canvas = tk.Canvas(root, width=COLS*CELL, height=ROWS*CELL)
canvas.pack()

def draw_cell(r, c, color):
    canvas.create_rectangle(
        c*CELL, r*CELL,
        (c+1)*CELL, (r+1)*CELL,
        fill=color, outline="gray"
    )
    root.update()
    time.sleep(0.02)

def draw_maze():
    for r in range(ROWS):
        for c in range(COLS):
            draw_cell(r, c, "black" if maze[r][c] == 1 else "white")

# ================= HEURISTIC =================
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# ================= BEST FIRST SEARCH =================
def best_first_search():
    pq = []
    heapq.heappush(pq, (heuristic(START, GOAL), START))
    visited = {START: None}

    while pq:
        _, (r, c) = heapq.heappop(pq)

        if (r, c) != START:
            draw_cell(r, c, "lightblue")

        if (r, c) == GOAL:
            break

        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if maze[nr][nc] == 0 and (nr, nc) not in visited:
                    visited[(nr, nc)] = (r, c)
                    h = heuristic((nr, nc), GOAL)
                    heapq.heappush(pq, (h, (nr, nc)))

    # Draw final path
    node = GOAL
    while node:
        r, c = node
        draw_cell(r, c, "red")
        node = visited[node]

# ================= RUN =================
draw_maze()
draw_cell(*START, "green")
draw_cell(*GOAL, "blue")
best_first_search()
root.mainloop()

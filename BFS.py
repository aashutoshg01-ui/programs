import tkinter as tk
from collections import deque
import time

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
CELL = 50

# ================= GUI =================
root = tk.Tk()
root.title("Animated BFS Maze Solver")
canvas = tk.Canvas(root, width=COLS*CELL, height=ROWS*CELL)
canvas.pack()

def draw_maze():
    for r in range(ROWS):
        for c in range(COLS):
            color = "black" if maze[r][c] == 1 else "white"
            canvas.create_rectangle(
                c*CELL, r*CELL,
                (c+1)*CELL, (r+1)*CELL,
                fill=color, outline="gray"
            )

def draw_cell(r, c, color):
    canvas.create_rectangle(
        c*CELL, r*CELL,
        (c+1)*CELL, (r+1)*CELL,
        fill=color, outline="gray"
    )
    root.update()
    time.sleep(0.05)

# ================= BFS WITH ANIMATION =================
def animated_bfs():
    queue = deque([START])
    visited = {START: None}

    while queue:
        r, c = queue.popleft()

        if (r, c) != START:
            draw_cell(r, c, "lightblue")  # explored

        if (r, c) == GOAL:
            break

        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if maze[nr][nc] == 0 and (nr, nc) not in visited:
                    visited[(nr, nc)] = (r, c)
                    queue.append((nr, nc))

    # draw final path
    if GOAL in visited:
        node = GOAL
        while node:
            r, c = node
            draw_cell(r, c, "red")
            node = visited[node]

# ================= RUN =================
draw_maze()

# start & goal
draw_cell(*START, "green")
draw_cell(*GOAL, "blue")

animated_bfs()
root.mainloop()
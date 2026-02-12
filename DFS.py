import tkinter as tk
import time

# ================= BIG COMPLEX MAZE =================
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
root.title("Animated DFS Maze Solver (Big Maze)")
canvas = tk.Canvas(root, width=COLS*CELL, height=ROWS*CELL)
canvas.pack()

def draw_cell(r, c, color):
    canvas.create_rectangle(
        c*CELL, r*CELL,
        (c+1)*CELL, (r+1)*CELL,
        fill=color, outline="gray"
    )
    root.update()
    time.sleep(0.03)

def draw_maze():
    for r in range(ROWS):
        for c in range(COLS):
            color = "black" if maze[r][c] == 1 else "white"
            draw_cell(r, c, color)

# ================= ANIMATED DFS =================
def animated_dfs():
    stack = [START]
    visited = {START: None}

    while stack:
        r, c = stack.pop()

        if (r, c) != START:
            draw_cell(r, c, "lightblue")

        if (r, c) == GOAL:
            break

        # Direction order matters a lot in DFS
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if maze[nr][nc] == 0 and (nr, nc) not in visited:
                    visited[(nr, nc)] = (r, c)
                    stack.append((nr, nc))
 
    # Draw final path (may not be shortest)
    if GOAL in visited:
        node = GOAL
        while node:
            r, c = node
            draw_cell(r, c, "red")
            node = visited[node]

# ================= RUN =================
draw_maze()
draw_cell(*START, "green")
draw_cell(*GOAL, "blue")
animated_dfs()
root.mainloop()
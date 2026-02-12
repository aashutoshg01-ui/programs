import tkinter as tk
import time
import heapq

# ================= BIG COMPLEX MAZE =================
maze = [
    [0,0,1,0,0,0,1,0,0,0,1,0,0,0,0],
    [1,0,1,0,1,0,1,0,1,0,1,0,1,1,0],
    [1,0,0,0,1,0,0,0,1,0,0,0,0,1,0],
    [1,1,1,0,1,1,1,0,1,1,1,1,0,1,0],
    [0,0,0,0,0,0,1,0,0,0,0,1,0,0,0],
    [0,1,1,1,1,0,1,1,1,1,0,1,1,1,0],
    [0,1,0,0,0,0,0,0,0,1,0,0,0,1,0],
    [0,1,0,1,1,1,1,1,0,1,1,1,0,1,0],
    [0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
    [0,1,0,1,0,1,0,1,1,1,0,1,0,1,0],
    [0,0,0,1,0,1,0,0,0,0,0,1,0,0,0],
    [1,1,0,1,0,1,1,1,1,1,1,1,0,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]


ROWS = len(maze)
COLS = len(maze[0])
START = (0, 0)
GOAL = (ROWS - 1, COLS - 1)
CELL = 35

# ================= GUI =================
root = tk.Tk()
root.title("Animated Uniform Cost Search (UCS)")
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

# ================= UNIFORM COST SEARCH =================
def animated_ucs():
    pq = []
    heapq.heappush(pq, (0, START))  # (cost, node)

    visited = {START: None}
    cost_so_far = {START: 0}

    while pq:
        current_cost, (r, c) = heapq.heappop(pq)

        if (r, c) != START:
            draw_cell(r, c, "lightblue")

        if (r, c) == GOAL:
            break

        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if maze[nr][nc] == 0:
                    new_cost = current_cost + 1
                    if (nr, nc) not in cost_so_far or new_cost < cost_so_far[(nr, nc)]:
                        cost_so_far[(nr, nc)] = new_cost
                        visited[(nr, nc)] = (r, c)
                        heapq.heappush(pq, (new_cost, (nr, nc)))

    # Draw final shortest path
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
animated_ucs()
root.mainloop()
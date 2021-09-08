num_of_rows = int(input())
row = []
maze = []
start = 0
num_of_moves = 0
is_escaped = False

for i in range(num_of_rows):
    row = list(input())
    maze.extend(row)

for i in range(len(maze)):
    if maze[i] == "k":
        start = i

while True:
    for i in range(len(maze)):
        if maze[i] == "k":
            if i % len(row) == 0:
                num_of_moves += 1
                is_escaped = True
                break
            elif (i + 1) % len(row) == 0:
                num_of_moves += 1
                is_escaped = True
                break
            elif i - len(row) not in range(len(maze)):
                num_of_moves += 1
                is_escaped = True
                break
            elif i + len(row) not in range(len(maze)):
                num_of_moves += 1
                is_escaped = True
                break
            elif maze[i - 1] == " ":
                maze[i - 1] = "k"
                maze[i] = "@"
                num_of_moves += 1
                break
            elif maze[i + 1] == " ":
                maze[i + 1] = "k"
                maze[i] = "@"
                num_of_moves += 1
                break
            elif maze[i - len(row)] == " ":
                maze[i - len(row)] = "k"
                maze[i] = "@"
                num_of_moves += 1
                break
            elif maze[i + len(row)] == " ":
                maze[i + len(row)] = "k"
                maze[i] = "@"
                num_of_moves += 1
                break
            else:
                if maze[start - 1] == " ":
                    i = start - 1
                    num_of_moves = 1
                    maze[start] = "*"
                    for k in range(len(maze)):
                        if maze[k] == "@" or maze[k] == "k":
                            maze[k] = " "
                    maze[i] = "k"
                elif maze[start + 1] == " ":
                    i = start + 1
                    num_of_moves = 1
                    maze[start] = "*"
                    for k in range(len(maze)):
                        if maze[k] == "@" or maze[k] == "k":
                            maze[k] = " "
                    maze[i] = "k"
                elif maze[start - len(row)] == " ":
                    i = start + len(row)
                    num_of_moves = 1
                    maze[start] = "*"
                    for k in range(len(maze)):
                        if maze[k] == "@" or maze[k] == "k":
                            maze[k] = " "
                    maze[i] = "k"
                elif maze[start + len(row)] == " ":
                    i = start + len(row)
                    num_of_moves = 1
                    maze[start] = "*"
                    for k in range(len(maze)):
                        if maze[k] == "@" or maze[k] == "k":
                            maze[k] = " "
                    maze[i] = "k"
                else:
                    print("Kate cannot get out")
                    exit(0)

    if is_escaped:
        break

print(f"Kate got out in {num_of_moves} moves")

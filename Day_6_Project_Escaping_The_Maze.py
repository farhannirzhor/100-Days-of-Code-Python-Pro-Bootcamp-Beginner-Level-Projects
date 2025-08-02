def is_valid_move(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != "#"

def play_maze():
    maze = [
        ['S', '.', '#'],
        ['.', '#', '.'],
        ['.', '.', 'E']
    ]

    x, y = 0, 0

    print("Welcome to the Maze Escape Game!")
    print("You're at the starting point (S). Reach the Exit (E).")
    print("You can move: north, south, east, west")

    while maze[x][y] != 'E':
        move = input("Enter your move: ").lower()

        new_x, new_y = x, y

        if move == "north":
            new_x -= 1
        elif move == "south":
            new_x += 1
        elif move == "east":
            new_y += 1
        elif move == "west":
            new_y -= 1
        else:
            print("Invalid move. Use north, south, east, or west.")
            continue

        if is_valid_move(new_x, new_y, maze):
            x, y = new_x, new_y
            print(f"You moved to ({x}, {y})")
        else:
            print("You hit a wall or boundary! Try a different direction.")

    print("🎉 Congratulations! You escaped the maze!")

play_maze()

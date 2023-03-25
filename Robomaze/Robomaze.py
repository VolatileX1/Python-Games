import random

# Define the size of the maze
MAZE_SIZE = 15

# Generate a random maze as a nested list of strings
maze = []
for i in range(MAZE_SIZE):
    row = ['#'] * MAZE_SIZE
    maze.append(row)

for i in range(1, MAZE_SIZE-1):
    for j in range(1, MAZE_SIZE-1):
        if random.random() < 0.7:
            maze[i][j] = ' '
            
# Define the robot's starting position and direction
robot_row = 1
robot_col = 1
robot_dir = "right"

# Define a function to print the maze with the robot's position
def print_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if row == robot_row and col == robot_col:
                # Print the robot instead of the maze character
                if robot_dir == "up":
                    print("^", end="")
                elif robot_dir == "down":
                    print("v", end="")
                elif robot_dir == "left":
                    print("<", end="")
                elif robot_dir == "right":
                    print(">", end="")
            else:
                print(maze[row][col], end="")
        print()

# Define a function to move the robot forward
def move_forward():
    global robot_row, robot_col
    if robot_dir == "up":
        if maze[robot_row-1][robot_col] == " ":
            robot_row -= 1
    elif robot_dir == "down":
        if maze[robot_row+1][robot_col] == " ":
            robot_row += 1
    elif robot_dir == "left":
        if maze[robot_row][robot_col-1] == " ":
            robot_col -= 1
    elif robot_dir == "right":
        if maze[robot_row][robot_col+1] == " ":
            robot_col += 1

# Define a function to turn the robot left
def turn_left():
    global robot_dir
    if robot_dir == "up":
        robot_dir = "left"
    elif robot_dir == "down":
        robot_dir = "right"
    elif robot_dir == "left":
        robot_dir = "down"
    elif robot_dir == "right":
        robot_dir = "up"

# Define a function to turn the robot right
def turn_right():
    global robot_dir
    if robot_dir == "up":
        robot_dir = "right"
    elif robot_dir == "down":
        robot_dir = "left"
    elif robot_dir == "left":
        robot_dir = "up"
    elif robot_dir == "right":
        robot_dir = "down"

# Play the game until the robot reaches the end of the maze
while robot_row != MAZE_SIZE-2 or robot_col != MAZE_SIZE-2:
    print_maze()
    print("Enter 'f' to move forward, 'l' to turn left, or 'r' to turn right.")
    user_input = input()
    if user_input == "f":
        move_forward()
    elif user_input == "l":
        turn_left()
    elif user_input == "r":
        turn_right()

# The robot has reached the end of the maze!
print("Congratulations, you have reached the end of the maze!")
print_maze()

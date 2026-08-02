import pygame
import sys

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game - Advanced")

# Colors
WHITE = (255, 255, 255)
BLACK = (5, 10, 25)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)

# Bigger Maze layout (More paths)
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,1,0,1,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,0,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,1,0,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]


player_x = 1
player_y = 1


player_color = RED

clock = pygame.time.Clock()

def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            if maze[row][col] == 1:
                pygame.draw.rect(screen,BLACK,
                                 (x, y, CELL_SIZE, CELL_SIZE))

            elif maze[row][col] == 2:
                pygame.draw.rect(screen, GREEN,
                                 (x, y, CELL_SIZE, CELL_SIZE))

    # Draw Player
    pygame.draw.rect(
        screen,
        player_color,
        (player_x * CELL_SIZE,
         player_y * CELL_SIZE,
         CELL_SIZE,
         CELL_SIZE)
    )

# Game loop
while True:

    screen.fill(WHITE)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            new_x = player_x
            new_y = player_y

            if event.key == pygame.K_UP:
                new_y -= 1

            if event.key == pygame.K_DOWN:
                new_y += 1

            if event.key == pygame.K_LEFT:
                new_x -= 1

            if event.key == pygame.K_RIGHT:
                new_x += 1

            if maze[new_y][new_x] != 1:
                player_x = new_x
                player_y = new_y

            if maze[player_y][player_x] == 2:
                print(" You reached the goal!")
                player_color = PURPLE

    draw_maze()

    pygame.display.update()

    clock.tick(10)
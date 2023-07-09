import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set the dimensions of the screen
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Game")

# Define the player's properties
player_size = 20
player_pos = [screen_width // 2, screen_height - player_size * 2]

# Define the maze
maze = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X                       X",
    "X XXXXXXXXXXXXXXXXXXXXX X",
    "X X                     X",
    "X X XXXXXXXXXXXXXXXXXXX X",
    "X X           X         X",
    "X XXXXXXXXXXX X XXXXXXX X",
    "X        X    X X       X",
    "X XXXXXX XXXX X X XXXXX X",
    "X             X   X     X",
    "X XXXXXXXXX XXXXXXX X X X",
    "X         X         X X X",
    "XXXXXXXXX XXXXXXXXXXX X X",
    "X         X           X X",
    "X XXXX XXXXXXXXXXX X X X",
    "X   X          X    X X X",
    "X X X XXXXXX X X XXXX X X",
    "X X X X      X X      X X",
    "X X X X XXXXXX XXXXXXXX X",
    "X X X X                X",
    "X X XXXXXXXXXXXXXXXXXXX X",
    "X X                   X X",
    "X XXXXXXXXXXXXXXXXXXX X X",
    "X                     X X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

# Define item properties
item_size = 10
item_color = GREEN
items = []
num_items = 5

# Create random item positions
for _ in range(num_items):
    x = random.randint(0, screen_width - item_size)
    y = random.randint(0, screen_height - item_size)
    items.append(pygame.Rect(x, y, item_size, item_size))

# Define goal properties
goal_size = 30
goal_color = GREEN
goal_pos = pygame.Rect(
    screen_width - goal_size, screen_height - goal_size, goal_size, goal_size
)

# Game loop
game_over = False
score = 0
time_limit = 60  # seconds
start_time = pygame.time.get_ticks()

while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size
            elif event.key == pygame.K_UP:
                y -= player_size
            elif event.key == pygame.K_DOWN:
                y += player_size

            # Check for collision with maze walls
            if (
                0 <= x < screen_width
                and 0 <= y < screen_height
                and maze[y // player_size][x // player_size] == "X"
            ):
                continue  # Ignore the move

            player_pos[0] = x
            player_pos[1] = y

    # Check for collisionwith items
    for item in items:
        if player_pos[0] == item.x and player_pos[1] == item.y:
            items.remove(item)
            score += 1

    # Check for collision with the goal
    if player_pos[0] == goal_pos.x and player_pos[1] == goal_pos.y:
        game_over = True

    # Check for game over condition (time limit)
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    if elapsed_time >= time_limit:
        game_over = True

    # Clear the screen
    screen.fill(BLACK)

    # Draw the maze
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "X":
                pygame.draw.rect(
                    screen,
                    WHITE,
                    (col * player_size, row * player_size, player_size, player_size),
                )

    # Draw the items
    for item in items:
        pygame.draw.rect(screen, item_color, item)

    # Draw the goal
    pygame.draw.rect(screen, goal_color, goal_pos)

    # Draw the player
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    # Display the score and time
    font = pygame.font.Font(None, 24)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    time_text = font.render(
        f"Time: {max(time_limit - elapsed_time, 0)} seconds", True, WHITE
    )
    screen.blit(time_text, (screen_width - 160, 10))

    # Update the display
    pygame.display.update()

# Game over screen
screen.fill(BLACK)
font = pygame.font.Font(None, 36)
game_over_text = font.render("Game Over", True, RED)
score_text = font.render(f"Final Score: {score}", True, WHITE)
screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 50))
screen.blit(score_text, (screen_width // 2 - 100, screen_height // 2))
pygame.display.update()

# Wait for a few seconds before quitting
pygame.time.wait(3000)

# Quit the game
pygame.quit()
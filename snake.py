import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen dimensions
width = 600
height = 400

# Create the game window
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game by ChatGPT')

# Clock to control the speed of the snake
clock = pygame.time.Clock()

snake_block = 10  # Size of the snake block
snake_speed = 15  # Speed of the snake

# Font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the player's score
def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    game_window.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, green, [x[0], x[1], snake_block, snake_block])

# Function to display a message on the screen
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [width / 6, height / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x = width / 2
    y = height / 2

    # Change in position
    x_change = 0
    y_change = 0

    # List to store the snake's body
    snake_list = []
    snake_length = 1

    # Random position for food
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_window.fill(blue)
            display_message("You Lost! Press Q-Quit or C-Play Again", red)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # If the snake goes out of bounds, the game ends
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        game_window.fill(black)

        # Draw the food
        pygame.draw.rect(game_window, yellow, [food_x, food_y, snake_block, snake_block])

        # Add the snake's new position to the list
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        # If the snake grows, remove the last part of the tail
        if len(snake_list) > snake_length:
            del snake_list[0]

        # If the snake collides with itself, the game ends
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        # If the snake eats the food, generate new food and grow the snake
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()

import pygame
import random

# initialize Pygame
pygame.init()

# set up game window
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Unique Snake Game')

# set up game variables
snake_size = 10
food_size = 15
score = 0

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# define fonts
font_40 = pygame.font.SysFont(None, 40)
font_60 = pygame.font.SysFont(None, 60)

# define functions
def draw_snake(snake_list):
    for x_and_y in snake_list:
        pygame.draw.rect(game_window, green, [x_and_y[0], x_and_y[1], snake_size, snake_size])

def draw_food(food_position):
    pygame.draw.circle(game_window, red, food_position, food_size)

def display_score(score):
    score_text = font_40.render('Score: ' + str(score), True, white)
    game_window.blit(score_text, [10, 10])

def display_game_over_message():
    game_over_text = font_60.render('Game Over!', True, white)
    game_window.blit(game_over_text, [window_width/2 - game_over_text.get_width()/2, window_height/2 - game_over_text.get_height()/2])
    pygame.display.update()
    pygame.time.wait(2000)

# set up game loop
clock = pygame.time.Clock()

def game_loop():

    # set up initial snake position and movement
    start_x = random.randrange(0, window_width - snake_size, 10)
    start_y = random.randrange(0, window_height - snake_size, 10)
    snake_list = [[start_x, start_y]]
    direction = 'right'

    # set up initial food position
    food_position = [random.randrange(food_size, window_width - food_size), random.randrange(food_size, window_height - food_size)]

    # start game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # change direction based on arrow key inputs
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'right':
                    direction = 'left'
                elif event.key == pygame.K_RIGHT and direction != 'left':
                    direction = 'right'
                elif event.key == pygame.K_UP and direction != 'down':
                    direction = 'up'
                elif event.key == pygame.K_DOWN and direction != 'up':
                    direction = 'down'

        # move snake
        if direction == 'right':
            new_x = snake_list[-1][0] + snake_size
            new_y = snake_list[-1][1]
        elif direction == 'left':
            new_x = snake_list[-1][0] - snake_size
            new_y = snake_list[-1][1]
        elif direction == 'down':
            new_x = snake_list[-1][0]
            new_y = snake_list[-1][1] + snake_size
        elif direction == 'up':
            new_x = snake_list[-1][0]
            new_y = snake_list[-1][1] - snake_size

        # check if snake hits wall or self
        if new_x >= window_width or new_x < 0 or new_y >= window_height or new_y < 0 or [new_x, new_y] in snake_list[:-1]:
            display_game_over_message()
            game_loop()

        # check if snake eats food
        if abs(new_x - food_position[0]) < food_size and abs(new_y - food_position[1]) < food_size:
            score += 1
            snake_list.append([new_x, new_y])
            food_position = [random.randrange(food_size, window_width - food_size), random.randrange(food_size, window_height - food_size)]

        else:
            snake_list.append([new_x, new_y])
            del snake_list[0]

        # draw game elements
        game_window.fill(black)
        draw_snake(snake_list)
        draw_food(food_position)
        display_score(score)

        # update game window
        pygame.display.update()

        # set game speed
        clock.tick(10)

# start game
game_loop()

# quit Pygame
pygame.quit()

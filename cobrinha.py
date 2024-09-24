import pygame
import sys
import random

#inicialização
pygame.init()

#janela
window_size = (400, 400)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Snake Game")

#cores
red = (210, 4, 45)
black = (0, 0, 0)
yellow = (255, 234, 0)

#bloco e velocidade
block_size = 20
speed = 10

#controle FPS
clock = pygame.time.Clock()

#desenho snake
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(window, yellow, pygame.Rect(segment[0], segment[1], block_size, block_size))

#função do jogo
def game():
    snake = [[100, 100]]
    direction = [block_size, 0] #começa p/ a direita
    food = [random.randrange(0, window_size[0] - block_size, block_size),
            random.randrange(0, window_size[1] - block_size, block_size)]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction[1] == 0:
                    direction = [0, -block_size]
                elif event.type == pygame.K_DOWN and direction[1] == 0:
                    direction = [0, block_size]
                elif event.type == pygame.K_LEFT and direction[0] == 0:
                    direction = [-block_size, 0]
                elif event.type == pygame.K_RIGHT and direction[0] == 0:
                    direction = [block_size, 0]
        
        new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
        snake.insert(0, new_head)

        if snake[0] == food:
            food = [random.randrange(0, window_size[0] - block_size, block_size),
                    random.randrange(0, window_size[1] - block_size, block_size)]
            
        else:
            snake.pop()

        window.fill(black)
        pygame.draw.rect(window, red, pygame.Rect(food[0], food[1], block_size, block_size))
        draw_snake(snake)

        pygame.display.flip()
        clock.tick(speed)

game()
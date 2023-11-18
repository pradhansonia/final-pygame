import unittest
import pygame
import time
import random
from snake_game import mixer

class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        # Initialize necessary variables for testing
        # You may need to adjust this based on your actual implementation
        self.window_x = 720
        self.window_y = 480
        self.snake_position = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.fruit_position = [200, 200]
        self.score = 0
        self.white = (255, 255, 255)

    def test_check_collision_game_over(self):
        # Test the game over conditions when snake hits the window boundaries
        self.snake_position = [-1, 50]
        self.assertTrue(check_collision(self.snake_position, self.snake_body, self.window_x, self.window_y))
        
        self.snake_position = [721, 50]
        self.assertTrue(check_collision(self.snake_position, self.snake_body, self.window_x, self.window_y))

        self.snake_position = [100, -1]
        self.assertTrue(check_collision(self.snake_position, self.snake_body, self.window_x, self.window_y))

        self.snake_position = [100, 481]
        self.assertTrue(check_collision(self.snake_position, self.snake_body, self.window_x, self.window_y))

    def test_check_collision_not_game_over(self):
        # Test when the snake doesn't hit the window boundaries
        self.snake_position = [100, 50]
        self.assertFalse(check_collision(self.snake_position, self.snake_body, self.window_x, self.window_y))

    def test_check_collision_snake_body(self):
        # Test the game over condition when the snake collides with its own body
        self.snake_position = [90, 50]
        self.assertTrue(check_collision(self.snake_position, self.snake_body, self.window_x, self.window_y))

    def test_show_score(self):
        # Test if the score is displayed correctly
        self.assertEqual(show_score(self.score, self.white, 'times new roman', 20), 'Score: 0')

        if __name__ == '__main__':
            unittest.main()

    def initialize_game():
        global snake_position, direction, change_to, snake_body, score, fruit_spawn, fruit_position
        snake_position = [100, 50]
        direction = 'RIGHT'
        change_to = 'RIGHT'
        snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        score = 0
        fruit_spawn = True
        fruit_position = [200, 200]

    def handle_key_events():
        global change_to, direction
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    def move_snake():
        global snake_position, direction, snake_body, fruit_position, fruit_spawn, score
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        elif change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        elif change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        elif change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_position[1] -= 10
        elif direction == 'DOWN':
            snake_position[1] += 10
        elif direction == 'LEFT':
            snake_position[0] -= 10
        elif direction == 'RIGHT':
            snake_position[0] += 10

    def check_collision():
        global snake_position, snake_body, fruit_position, fruit_spawn, score
        if snake_position[0] < 0 or snake_position[0] > window_x - 10 or \
        snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False

    def draw_elements():
        global snake_body, fruit_position
        snake_body.insert(0, list(snake_position))
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

        fruit_spawn = True
        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    def display_score():
        global score
        show_score(1, white, 'times new roman', 20)

    def game_loop():
        while True:
            handle_key_events()
            move_snake()
            check_collision()
            draw_elements()
            display_score()
            pygame.display.update()
            fps.tick(snake_speed)

# Additional functions for Pygame initialization can be added as needed.
if __name__ == '__main__':
        initialize_game()
        game_loop()

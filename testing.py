import unittest
import snake_game
from main import mixer

class SnakeGameTests(unittest.TestCase):

    def test_draw_single_block(self):
        # Test that draw_single_block draws a block of the correct size and color at the correct position
        block_position = [10, 20]
        block_color = (255, 0, 0)

        snake_game.draw_single_block(block_position, block_color)

        # Check that the block is the correct size
        self.assertEqual(surface.get_width_at(block_position[0]), SNAKE_SQUARE_DIMENSIONS)
        self.assertEqual(surface.get_height_at(block_position[1]), SNAKE_SQUARE_DIMENSIONS)

        # Check that the block is the correct color
        self.assertEqual(surface.get_at(block_position), block_color)

    def test_move_block(self):
        # Test that move_block moves the block in the correct direction
        original_position = [10, 20]
        new_position = None

        # Move the block to the left
        new_position = snake_game.move_block(original_position[0], original_position[1], "LEFT")
        self.assertEqual(new_position[0], original_position[0] - 1)
        self.assertEqual(new_position[1], original_position[1])

        # Move the block to the right
        new_position = snake_game.move_block(original_position[0], original_position[1], "RIGHT")
        self.assertEqual(new_position[0], original_position[0] + 1)
        self.assertEqual(new_position[1], original_position[1])

        # Move the block up
        new_position = snake_game.move_block(original_position[0], original_position[1], "UP")
        self.assertEqual(new_position[0], original_position[0])
        self.assertEqual(new_position[1], original_position[1] - 1)

        # Move the block down
        new_position = snake_game.move_block(original_position[0], original_position[1], "DOWN")
        self.assertEqual(new_position[0], original_position[0])
        self.assertEqual(new_position[1], original_position[1] + 1)

    def test_detect_direction(self):
        # Test that detect_direction detects the correct direction based on the key pressed
        event = pygame.event.Event(type=pygame.KEYDOWN)

        # Test the left arrow key
        event.key = pygame.K_LEFT
        direction = snake_game.detect_direction(None, event)
        self.assertEqual(direction, "LEFT")

        # Test the right arrow key
        event.key = pygame.K_RIGHT
        direction = snake_game.detect_direction(None, event)
        self.assertEqual(direction, "RIGHT")

        # Test the up arrow key
        event.key = pygame.K_UP
        direction = snake_game.detect_direction(None, event)
        self.assertEqual(direction, "UP")

        # Test the down arrow key
        event.key = pygame.K_DOWN
        direction = snake_game.detect_direction(None, event)
        self.assertEqual(direction, "DOWN")

if _name_ == "_main_":
    unittest.main()
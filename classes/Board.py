import pygame
import sys


class Board:
    def __init__(
        self,
        rows=8,
        cols=8,
        cell_size=60,
        knight_image=pygame.image.load("knight.png"),
        margin=20,
    ):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.margin = margin
        self.knight_image = pygame.transform.scale(knight_image, (cell_size, cell_size))
        self.knight_position = (0, 0)  # Initial position
        self.move_counter = 1
        self.visited_cells = [[0] * cols for _ in range(rows)]

    def draw_board(self, screen):
        # Draw the board background
        screen.fill((238, 238, 210))

        # Draw the board cells
        for row in range(self.rows):
            for col in range(self.cols):
                cell_rect = pygame.Rect(
                    col * self.cell_size + 2 * self.margin,
                    row * self.cell_size + 2 * self.margin,
                    self.cell_size,
                    self.cell_size,
                )
                color = (238, 238, 210) if (row + col) % 2 == 0 else (118, 150, 85)
                pygame.draw.rect(screen, color, cell_rect)

                # Draw a low-opacity rectangle for visited cells
                if self.visited_cells[row][col] > 0:
                    visited_rect = pygame.Surface(
                        (self.cell_size, self.cell_size), pygame.SRCALPHA
                    )
                    visited_rect.fill((153, 176, 77, 100))
                    screen.blit(
                        visited_rect,
                        (
                            col * self.cell_size + 2 * self.margin,
                            row * self.cell_size + 2 * self.margin,
                        ),
                    )

                    font = pygame.font.Font(None, 24)
                    text = font.render(
                        str(self.visited_cells[row][col]), True, (0, 0, 0)
                    )
                    screen.blit(
                        text,
                        (
                            col * self.cell_size
                            + 2 * self.margin
                            + self.cell_size // 3,
                            row * self.cell_size
                            + 2 * self.margin
                            + self.cell_size // 3,
                        ),
                    )

        # draw a border around the board
        border_rect = pygame.Rect(
            2 * self.margin,
            2 * self.margin,
            self.cols * self.cell_size,
            self.rows * self.cell_size,
        )

        pygame.draw.rect(screen, (142, 161, 113), border_rect, 1)

        # Draw the row numbers
        font = pygame.font.Font(None, 24)
        for row in range(self.rows):
            text = font.render(str(row), True, (142, 161, 113))
            screen.blit(
                text,
                (
                    2 * self.margin // 2,
                    row * self.cell_size + 2 * self.margin + self.cell_size // 3,
                ),
            )

        # Draw the column numbers
        for col in range(self.cols):
            text = font.render(str(col), True, (142, 161, 113))
            screen.blit(
                text,
                (
                    col * self.cell_size + 2 * self.margin + self.cell_size // 3,
                    2 * self.margin // 2,
                ),
            )

        # Draw the knight at its current position
        knight_rect = pygame.Rect(
            self.knight_position[1] * self.cell_size + 2 * self.margin,
            self.knight_position[0] * self.cell_size + 2 * self.margin,
            self.cell_size,
            self.cell_size,
        )
        screen.blit(self.knight_image, knight_rect)

    def move_knight(self, row, col):
        self.knight_position = (row, col)
        self.visited_cells[row][col] = self.move_counter
        self.move_counter += 1

    def main(self, knight_path):
        pygame.init()

        # Set up display
        width, height = (self.cols + 1) * self.cell_size + self.margin, (
            self.rows + 1
        ) * self.cell_size + self.margin
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Knight's Tour")

        for position in knight_path:
            self.move_knight(*position)

            # Draw the board with the knight and the path
            self.draw_board(screen)

            pygame.display.flip()
            pygame.time.delay(500)  # Pause for a short duration to visualize each move

        # Wait for the user to close the window
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

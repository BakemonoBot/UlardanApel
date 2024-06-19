import tkinter
import random  

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SnakeSegment(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = 'lime green'

class Food(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = 'red'

class Snake:
    def __init__(self, initial_length=3):
        self.head = SnakeSegment(TILE_SIZE * 5, TILE_SIZE * 5)
        self.body = []
        self.direction = 'Right'  

        for i in range(1, initial_length):
            self.body.append(SnakeSegment(self.head.x - i * TILE_SIZE, self.head.y))

    def move(self):
        if self.body:
            for i in range(len(self.body) - 1, 0, -1):
                self.body[i].x = self.body[i - 1].x
                self.body[i].y = self.body[i - 1].y
            if self.direction == 'Up':
                self.head.y -= TILE_SIZE
            elif self.direction == 'Down':
                self.head.y += TILE_SIZE
            elif self.direction == 'Left':
                self.head.x -= TILE_SIZE
            elif self.direction == 'Right':
                self.head.x += TILE_SIZE

    def grow(self):
        if self.body:
            self.body.append(SnakeSegment(self.body[-1].x, self.body[-1].y))
        else:
            self.body.append(SnakeSegment(self.head.x - TILE_SIZE, self.head.y))

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(TILE_SIZE * 10, TILE_SIZE * 10)
        self.score = 0
        self.game_over = False

    def check_collision(self):
        if self.snake.head.x < 0 or self.snake.head.x >= WINDOW_WIDTH or self.snake.head.y < 0 or self.snake.head.y >= WINDOW_HEIGHT:
            self.game_over = True
        for segment in self.snake.body:
            if segment.x == self.snake.head.x and segment.y == self.snake.head.y:
                self.game_over = True

        if self.snake.head.x == self.food.x and self.snake.head.y == self.food.y:
            self.snake.grow()
            self.score += 1
            self.food.x = random.randint(0, COLS - 1) * TILE_SIZE
            self.food.y = random.randint(0, ROWS - 1) * TILE_SIZE

    def update(self):
        if not self.game_over:
            self.snake.move()
            self.check_collision()

    def restart(self):
        self.snake = Snake()
        self.food = Food(TILE_SIZE * 10, TILE_SIZE * 10)
        self.score = 0
        self.game_over = False

game = Game()

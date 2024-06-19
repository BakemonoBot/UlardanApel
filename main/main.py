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

window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg="black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

snake = Tile(TILE_SIZE * 5, TILE_SIZE * 5)
food = Tile(TILE_SIZE * 10, TILE_SIZE * 10)
velocityX = 0
velocityY = 0
snake_body = []
game_over = True
score = 0

welcome_text = canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 20, font="Arial 20", text="Selamat Datang Di Game, Ular Dan Apel", fill="white")
instruction_text = canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 20, font="Arial 15", text="Tekan 'm' untuk mulai", fill="white")

def change_direction(e):
    global game_over, velocityX, velocityY
    if game_over and e.keysym == "m":
        start_game()
    if not game_over:
        if e.char == "w" and velocityY != 1:
            velocityX = 0
            velocityY = -1
        elif e.char == "s" and velocityY != -1:
            velocityX = 0
            velocityY = 1
        elif e.char == "a" and velocityX != 1:
            velocityX = -1
            velocityY = 0
        elif e.char == "d" and velocityX != -1:
            velocityX = 1
            velocityY = 0

def start_game():
    global game_over, snake, snake_body, score
    canvas.delete(welcome_text)
    canvas.delete(instruction_text)
    snake = Tile(TILE_SIZE * 5, TILE_SIZE * 5)
    snake_body = []
    score = 0
    game_over = False
    draw()

def move():
    global snake, food, snake_body, game_over, score, velocityX, velocityY  
    if game_over:
        return

    if snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT:
        game_over = True
        return

    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            game_over = True
            return

    if snake_body:
        last_tile = snake_body[-1]
        last_x = last_tile.x
        last_y = last_tile.y
        last_tile.x = snake.x
        last_tile.y = snake.y

        for i in range(len(snake_body) - 2, -1, -1):
            current_tile = snake_body[i]
            temp_x = current_tile.x
            temp_y = current_tile.y
            current_tile.x = last_x
            current_tile.y = last_y
            last_x = temp_x
            last_y = temp_y

    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS-1) * TILE_SIZE
        food.y = random.randint(0, ROWS-1) * TILE_SIZE
        score += 1

    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE

def draw():
    global snake, food, snake_body, game_over, score
    move()
    canvas.delete("all")
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill='red')
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill='blue')
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill='lime green')
    if game_over:
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, font="Arial 20", text=f"Yah Cuma Dapet: {score}", fill="white")
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 30, font="Arial 15", text="Tekan 'm' untuk mulai lagi", fill="white")
    else:
        canvas.create_text(30, 20, font="Arial 10", text=f"Score: {score}", fill="white")
        window.after(100, draw)

window.bind("<Key>", change_direction)
window.mainloop()

import pgzrun
import random
from pygame import Rect

# Screen Size
WIDTH = 800
HEIGHT = 600

# Hero Class
class Hero:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed = 4
        self.sprites = ["hero_idle", "hero_walk1", "hero_walk2"]
        self.sprite = Actor(self.sprites[0], (self.x, self.y))
        self.frame = 0
    
    def move(self):
        moving = False
        if keyboard.left:
            self.x -= self.speed
            moving = True
        if keyboard.right:
            self.x += self.speed
            moving = True
        if keyboard.up:
            self.y -= self.speed
            moving = True
        if keyboard.down:
            self.y += self.speed
            moving = True
        
        if moving:
            self.frame = (self.frame + 1) % len(self.sprites)
            self.sprite.image = self.sprites[self.frame]
        else:
            self.sprite.image = self.sprites[0]
        
        self.sprite.pos = (self.x, self.y)
    
    def draw(self):
        self.sprite.draw()

# Enemy Class
class Enemy:
    def __init__(self, x, y, area):
        self.x = x
        self.y = y
        self.area = area
        self.direction = random.choice(["left", "right", "up", "down"])
        self.sprites = ["enemy_idle", "enemy_move1", "enemy_move2"]
        self.sprite = Actor(self.sprites[0], (self.x, self.y))
        self.frame = 0
    
    def move(self):
        if self.direction == "left":
            self.x -= 2
        elif self.direction == "right":
            self.x += 2
        elif self.direction == "up":
            self.y -= 2
        elif self.direction == "down":
            self.y += 2
        
        if not self.area.collidepoint(self.x, self.y):
            self.direction = random.choice(["left", "right", "up", "down"])
        
        self.frame = (self.frame + 1) % len(self.sprites)
        self.sprite.image = self.sprites[self.frame]
        self.sprite.pos = (self.x, self.y)
    
    def draw(self):
        self.sprite.draw()

# Menu
def draw_menu():
    screen.clear()
    screen.draw.text("MAIN MENU", center=(WIDTH // 2, HEIGHT // 4), fontsize=50, color="white")
    screen.draw.text("1. Start Game", center=(WIDTH // 2, HEIGHT // 2), fontsize=40, color="white")
    screen.draw.text("2. Toggle Sound", center=(WIDTH // 2, HEIGHT // 2 + 50), fontsize=40, color="white")
    screen.draw.text("3. Exit", center=(WIDTH // 2, HEIGHT // 2 + 100), fontsize=40, color="white")

game_running = False
sound_on = True

def on_key_down(key):
    global game_running, sound_on
    if not game_running:
        if key == keys.K_1:
            game_running = True
        elif key == keys.K_2:
            sound_on = not sound_on
        elif key == keys.K_3:
            exit()

def update():
    if game_running:
        hero.move()
        for enemy in enemies:
            enemy.move()

try:
    background = Actor("background", (WIDTH // 2, HEIGHT // 2))
except Exception as e:
    print(f"Background yüklenirken hata oluştu: {e}")


def draw():
    screen.clear()
    if game_running:
        background.draw()  # Arka planı çiz
        hero.draw()
        for enemy in enemies:
            enemy.draw()
    else:
        draw_menu()



# Game Initialization
hero = Hero()
enemies = [Enemy(random.randint(100, 700), random.randint(100, 500), Rect(100, 100, 600, 400)) for _ in range(2)]

pgzrun.go()
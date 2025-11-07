import pgzrun
import pygame
from pygame.mixer import music

WIDTH = 800
HEIGHT = 600
TITLE = "Reach The Flag"

game_state = "menu"
music_on = True


class Platform:
    def __init__(self, x, y, w, h):
        self.rect = Rect((x, y), (w, h))

    def draw(self):
        screen.draw.filled_rect(self.rect, (60, 60, 60))


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.speed = 4
        self.life = 100
        self.alive = True
        self.image = "knob"
        self.width = 50
        self.height = 50
        self.collision_cooldown = 0

    def move(self):
        # Movement controls
        self.vx = 0
        self.vy = 0

        if keyboard.left:
            self.vx = -self.speed
        elif keyboard.right:
            self.vx = self.speed
        if keyboard.up:
            self.vy = -self.speed
        elif keyboard.down:
            self.vy = self.speed

        self.x += self.vx
        self.y += self.vy

        # Stay within screen bounds
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > WIDTH:
            self.x = WIDTH - self.width
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > HEIGHT:
            self.y = HEIGHT - self.height

        # Update cooldown timer
        if self.collision_cooldown > 0:
            self.collision_cooldown -= 1

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def loseHealth(self, amount=10):
        # Prevent repeated damage from single collision
        if self.collision_cooldown <= 0:
            self.life -= amount
            self.collision_cooldown = 60
            if self.life <= 0:
                self.alive = False


class Enemy:
    def __init__(self, x, y, vx, vy, image="enemy_2"):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.width = 50
        self.height = 50
        self.image = image

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Bounce off screen edges
        if self.x <= 0 or self.x + self.width >= WIDTH:
            self.vx *= -1
        if self.y <= 0 or self.y + self.height >= HEIGHT:
            self.vy *= -1

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Goal:
    def __init__(self, x, y):
        self.rect = Rect((x, y), (60, 60))
        self.image = "fwin_flag"

    def draw(self):
        screen.blit(self.image, self.rect.topleft)


# Game objects
player = Player(50, HEIGHT - 80)
enemies = [
    Enemy(200, 200, 3, 2, image="enemy_2"),
    Enemy(500, 300, -2, 3, image="enemy_idle")
]
platforms = [Platform(0, HEIGHT - 20, WIDTH, 20)]
goal = Goal(WIDTH - 80, 20)


class Button:
    def __init__(self, rect, text, action):
        self.rect = Rect(rect)
        self.text = text
        self.action = action

    def draw(self):
        mx, my = pygame.mouse.get_pos()
        base_color = (70, 130, 180)
        hover_color = (100, 160, 210)
        color = hover_color if self.rect.collidepoint(mx, my) else base_color
        screen.draw.filled_rect(self.rect, color)
        screen.draw.text(self.text, center=self.rect.center, color=(255, 255, 255), fontsize=40)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.action()


def start_game():
    global game_state, player
    game_state = "playing"
    player.x, player.y = 50, HEIGHT - 80
    player.life = 100
    player.alive = True
    player.collision_cooldown = 0


def toggle_music():
    global music_on
    music_on = not music_on
    if music_on:
        music.load("sounds/bg_music.mp3")
        music.play(-1)
    else:
        music.stop()


def exit_game():
    quit()


buttons = [
    Button((WIDTH // 2 - 100, 200, 200, 60), "Start Game", start_game),
    Button((WIDTH // 2 - 100, 300, 200, 60), "Toggle Music", toggle_music),
    Button((WIDTH // 2 - 100, 400, 200, 60), "Exit", exit_game)
]


def update():
    global game_state
    if game_state == "playing":
        player.move()
        for enemy in enemies:
            enemy.move()
            if Rect((player.x, player.y), (player.width, player.height)).colliderect(
                Rect((enemy.x, enemy.y), (enemy.width, enemy.height))
            ):
                player.loseHealth()
                if music_on:
                    sounds.hit.play()

        # Check if player reached the goal
        if Rect((player.x, player.y), (player.width, player.height)).colliderect(goal.rect):
            game_state = "win"

        # Check if player ran out of health
        if not player.alive:
            game_state = "game_over"


def draw():
    screen.clear()
    if game_state == "menu":
        screen.fill((30, 30, 40))
        screen.draw.text("Reach The Flag", center=(WIDTH // 2, 100), color="white", fontsize=60)
        for b in buttons:
            b.draw()

    elif game_state == "playing":
        screen.fill((50, 50, 100))
        for p in platforms:
            p.draw()
        player.draw()
        for e in enemies:
            e.draw()
        goal.draw()
        screen.draw.text(f"Life: {player.life}", (10, 10), color="white", fontsize=30)

    elif game_state == "game_over":
        screen.fill((100, 0, 0))
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2), fontsize=80, color="white")
        screen.draw.text("Click to return to menu", center=(WIDTH // 2, HEIGHT // 2 + 80), fontsize=40, color="white")

    elif game_state == "win":
        screen.fill((0, 120, 0))
        screen.draw.text("YOU WIN!", center=(WIDTH // 2, HEIGHT // 2), fontsize=80, color="white")
        screen.draw.text("Click to return to menu", center=(WIDTH // 2, HEIGHT // 2 + 80), fontsize=40, color="white")


def on_mouse_down(pos):
    global game_state
    if game_state == "menu":
        for b in buttons:
            b.check_click(pos)
    elif game_state in ["game_over", "win"]:
        game_state = "menu"


# Initialize background music
if music_on:
    try:
        music.load("sounds/bg_music.mp3")
        music.play(-1)
    except Exception as e:
        print("Music file missing or invalid:", e)


pgzrun.go()
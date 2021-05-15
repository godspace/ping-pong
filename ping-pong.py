 
from sys import platform
from pygame import*
 
W = 666
H = 666
 
window = display.set_mode((W, H))
clock = time.Clock()
 
 
class GameSprites(sprite.Sprite):
    def __init__(self, file, width, height, x, y, xspeed, yspeed):
        sprite.Sprite.__init__(self)
        self.image = image.load(file)
        self.image = transform.scale(self.image,(width, height))
        self.rect = self.image.get_rect(centerx = x, centery = y)
        self.xspeed = xspeed
        self.yspeed = yspeed
    def draw(self):
        window.blit(self.image, self.rect)
 
class Ball(GameSprites):
    def move(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.x > W - self.rect.width or self.rect.x < 0:
            self.xspeed *= -1
        if self.rect.y > H - self.rect.height or self.rect.y < 0:
            self.yspeed *= -1
 
ball = Ball("ball.png", 50, 50, W//2, H//2, 10, 5)

class Player(GameSprites):
    def move_01(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.yspeed
        if keys[K_s]:
            self.rect.y += self.yspeed
    def move_02(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.yspeed
        if keys[K_DOWN]:
            self.rect.y += self.yspeed
    def collide_01(self):
        if sprite.collide_rect(self, ball):
            ball.xspeed = 10
    def collide_02(self):
        if sprite.collide_rect(self, ball):
            ball.xspeed = -10


player_01 = Player("player.png",40, 80, 40, H/2, 0, 10)
player_02 = Player("player.png",40, 80, W - 40, H/2, 0, 10)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            print(game, e.type)
    window.fill((235, 80, 67))
    ball.draw()
    ball.move()
    player_01.draw()
    player_01.move_01()
    player_01.collide_01()
    player_02.draw()
    player_02.move_02()
    player_02.collide_02()
    display.update()
    clock.tick(24)
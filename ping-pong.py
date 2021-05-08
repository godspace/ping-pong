from pygame import *

W = 800
H = 400
window = display.set_mode((W,H))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, file, x, y, w, h, x_speed, y_speed):
        #sprite.Sprite.__init__(self)
        super().__init__()
        self.image = image.load(file)
        self.image = transform.scale(self.image,(w, h))
        self.rect = self.image.get_rect(centerx=x, centery=y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def draw(self):
        window.blit(self.image,self.rect)

class Ball(GameSprite):
    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.x > W - self.rect.width or self.rect.x < 0:
            self.x_speed *= -1
        if self.rect.y > H - self.rect.height or self.rect.y < 0:
            self.y_speed *= -1

ball = Ball("ball.png",W//2,H//2,40,40,2,2)


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    window.fill((50,150,50))
    ball.draw()
    ball.move()
    display.update()
    clock.tick(100)
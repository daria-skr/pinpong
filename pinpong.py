import pygame as pg

from random import randint

class Base_sprite(pg.sprite.Sprite):
    def __init__(self, pic, x, y, w, h):
        super().__init__()
        self.picture = pg.transform.scale(
            pg.image.load(pic), (w, h)
        ) 
        self.image = self.picture
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        mw.blit(self.picture, (self.rect.x, self.rect.y))


class Player(Base_sprite):
    speed = 5

    def update_l(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed 
        if keys[pg.K_DOWN] and self.rect.y <= win_h - self.rect.height:            
            self.rect.y += self.speed 
            
    def update_r(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.rect.y >= 5:
            self.rect.y -= self.speed 
            
        if keys[pg.K_s] and self.rect.y <= win_h - self.rect.height:            
            self.rect.y += self.speed 
            

class Ball(Base_sprite):
    speed_x = 1
    speed_y = -1

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y -= self.speed_y
        if self.rect.y <= 0 or self.rect.y >= win_h - self.rect.height:
            self.speed_y *= -1
        
            
        
win_w = 700
win_h = 500


rocket_l = Player('ping_rocket1.png', 20, 350, 15, 60)
rocket_r = Player('ping_rocket2.png', 670, 350, 15, 60 )
ball = Ball('ball.png', win_w/2, win_h/2, 30, 30)


mw = pg.display.set_mode((win_w, win_h))
pg.display.set_caption('ПИНПОНГ')

clock = pg.time.Clock()

fon = pg.image.load('grass.jpg')
fon = pg.transform.scale(fon, (win_w, win_h))

ticks = 0

play = True
game  = True
while play:

    for e in pg.event.get():
        if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
            play = False


    if game:
        mw.blit(fon, (0, 0))


        rocket_l.update_l()
        rocket_r.update_r()
        ball.update()

        if ball.rect.colliderect(rocket_l.rect) or ball.rect.colliderect(rocket_r.rect):
            ball.speed_x *= -1

        rocket_l.draw()
        rocket_r.draw()
        ball.draw()


    pg.display.update()
    clock.tick(60)

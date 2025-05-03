#Создай собственный Шутер!

import pygame as pg

from random import randint

pg.init()
counter = 0
class BaseSprite(pg.sprite.Sprite):
    def __init__(self, filename, x, y, w, h, speed_x=0, speed_y=0,):
        super().__init__()
        self.rect = pg.Rect(x, y, w, h)
        self.image = pg.transform.scale(pg.image.load(filename), (w, h))
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class Hero(BaseSprite):
    energy = 0
    health = 200

    def update(self):
        self.energy += 1
        self.draw_health()
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > mw_size[x] - self.rect.width:
            self.rect.x = mw_size[x] - self.rect.width

        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > mw_size[y] - self.rect.height:
            self.rect.y = mw_size[y] - self.rect.height

    def draw_health(self):
        hp_bar = pg.Surface((long, 10))
        hp_bar.fill((red, green, 50))
        help_bar = pg.Surface((100, 10))
        help_bar.fill((225, 0, 0))
        mw.blit(help_bar, (ship.rect.x, ship.rect.y+ship.rect.h))
        mw.blit(hp_bar, (ship.rect.x, ship.rect.y+ship.rect.h))

    def fire(self):
        if self.energy >= 30:
            self.energy = 0
            w = 16
            h = 40
            bullet = Bullet('bullet.png', self.rect.x + self.rect.width/2 - w/2, self.rect.y - h, w, h, speed_x=0, speed_y=-5)
            fire.play()
            bullets.add(bullet)
            all_sprite.add(bullet)

class Star(BaseSprite):
    def update(self):
        super().update()
        if self.rect.y > mw_size[y]:
            self.kill()

class Meteor(pg.sprite.Sprite):
    def __init__(self, x, y, meteor_sprites, meteors, speed_x =0 , speed_y = 0) -> None:
        super().__init__()           
        self.frames = meteor_sprites
        self.frame_rate = 1   
        self.frame_num = 0
        self.image = meteor_sprites[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.add(meteors)
        self.add(all_sprite)
    
    def next_frame(self):
        self.image = self.frames[self.frame_num]
        self.frame_num += 1
        if self.frame_num > len(self.frames)-1:
            self.frame_num = 0
        
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.next_frame()

class UFO(BaseSprite):
    def update(self):
        global counter
        super().update()
        if self.rect.y > mw_size[y]:
            self.kill()
            counter += 1




class Bullet(BaseSprite):
    def update(self):
        super().update()
        if self.rect.y < -50:
            self.kill()

class Boom(pg.sprite.Sprite):
    def __init__(self, ufo_center, boom_sprites, booms) -> None:
        super().__init__() 
        #global booms, boom_sprites              
        self.frames = boom_sprites        
        self.frame_rate = 1   
        self.frame_num = 0
        self.image = boom_sprites[0]
        self.rect = self.image.get_rect()
        self.rect.center = ufo_center
        self.add(booms)
        self.add(all_sprite)
    
    def next_frame(self):
        self.image = self.frames[self.frame_num]
        self.frame_num += 1
        if self.frame_num > len(self.frames)-1:
            self.frame_num = 0
        
    
    def update(self):
        self.next_frame()
        if self.frame_num == len(self.frames)-1:
            self.kill()



def sprites_load(folder, file_name, size, colorkey=(0,0,0)):    
    sprites = []
    load = True
    num = 1
    while load:
        try:
            spr = pg.image.load(f'{folder}\\{file_name}{num}.png')
            spr = pg.transform.scale(spr,size)
            if colorkey: spr.set_colorkey(colorkey)
            sprites.append(spr)
            num += 1
        except:
            load = False
    return sprites

def set_text(text, x, y, color=(255, 255, 200)):
    mw.blit(font1.render(text, True, color),[x, y])

def spawn_star():
        size = randint(15, 40)
        star = Star('star.png', randint(0, mw_size[x]), -10, size, size, 0, randint(2, 9))
        stars.add(star)
        all_sprite.add(star)

def spawn_boss():
        boss = BaseSprite('boss.png', mw_size[x]/2, -25, 150, 100, 0, 5)
        all_sprite.add(boss)

def spawn_ufo():
        ufo = UFO('ufo.png', randint(0, mw_size[x]-70), -10, 70, 70, 0, randint(2, 4))
        ufoes.add(ufo)
        all_sprite.add(ufo)

def spawn_s_b():
        s_b = BaseSprite('speed_boost.png', randint(0, mw_size[x]-50), randint(0, mw_size[y]-50), 50, 50)
        speed_boosts.add(s_b)
        all_sprite.add(s_b)

def spawn_hp_b():
        hp_b = BaseSprite('hp_boost.png', randint(0, mw_size[x]-50), randint(0, mw_size[y]-50), 75, 50)
        hp_boosts.add(hp_b)
        all_sprite.add(hp_b)

def spawn_sh_b():
        sh_b = BaseSprite('shield.png', randint(0, mw_size[x]-50), randint(0, mw_size[y]-50), 50, 50)
        shield_boosts.add(sh_b)
        all_sprite.add(sh_b)

x, y = 0, 1

mw_size = (800, 600)
pg.display.set_caption('Шутер')
mw = pg.display.set_mode(mw_size)

background = pg.image.load('galaxy.jpg')
background = pg.transform.scale(background, mw_size)

fon_go = pg.image.load('fon_go.png')
fon_go = pg.transform.scale(fon_go, mw_size)

fon_win = pg.image.load('fon_win.png')
fon_win = pg.transform.scale(fon_win, mw_size)

clock = pg.time.Clock()

stars = pg.sprite.Group()
ufoes = pg.sprite.Group()
bullets = pg.sprite.Group()
speed_boosts = pg.sprite.Group()
hp_boosts = pg.sprite.Group()
shield_boosts = pg.sprite.Group()
booms = pg.sprite.Group()
meteors = pg.sprite.Group()
all_sprite = pg.sprite.Group()

ship = Hero("spaceship.png", 390, 490, 100, 100)
all_sprite.add(ship)

font1 = pg.font.Font(None, 40)

play = True
game = True
win = False
s_b_agr = True
ticks = 1
speed = 5
s_b_count = 0
long = 100
red = 0
green = 225
shield = False
sh_b_agr = True
sh_b_count = 0
killpoint = 0
ufo_arg = True
boss_arg = True

boom_sprites = sprites_load('boom4', 'boom', (80, 80))

meteor_sprites = [
    sprites_load('meteor1', 'meteor', (50, 50)),
    sprites_load('meteor1', 'meteor', (60, 60)),
    sprites_load('meteor1', 'meteor', (70, 70)),
    sprites_load('meteor1', 'meteor', (80, 80)),
    sprites_load('meteor1', 'meteor', (90, 0)),
]

pg.mixer.music.load('space.ogg')
pg.mixer.music.play()

fire = pg.mixer.Sound('fire.ogg')

while play:

    if game:

        if ticks % 8 == 0: 
            spawn_star()

        if ticks % 80 == 0: 
            Meteor(randint(0, mw_size[x]), -10, meteor_sprites[randint(0, 4)], meteors, randint(-2, 2), randint(2, 5)) 
            
        if ticks % 120 == 0 and ufo_arg == True: 
            spawn_ufo()

        # if killpoint == 1 and boss_arg == True:
        #     spawn_boss()
        #     boss_arg = False
        #     ufo_arg = False
        #     if boss.rect.y == 50:
        #         boss.speed_y = 0/boss.speed_y
        
        if ticks % 480 == 0 and s_b_agr == True:
            spawn_s_b()

        if ticks % 600 == 0:
            spawn_hp_b()

        if ticks % 540 == 0 and sh_b_agr == True:
            spawn_sh_b()
            
        mw.blit(background, (0, 0))
       
        for event in pg.event.get():
            if event.type == pg.QUIT:
                play = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    ship.speed_x = speed * -1
                if event.key == pg.K_RIGHT:
                    ship.speed_x = speed
                if event.key == pg.K_UP:
                    ship.speed_y = speed * -1
                if event.key == pg.K_DOWN:
                    ship.speed_y = speed
                if event.key == pg.K_SPACE:
                    ship.fire()
                    
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    ship.speed_x = 0
                if event.key == pg.K_RIGHT:
                    ship.speed_x = 0
                if event.key == pg.K_UP:
                    ship.speed_y = 0
                if event.key == pg.K_DOWN:
                    ship.speed_y = 0
        
        all_sprite.update()
        all_sprite.draw(mw)
    
        if pg.sprite.spritecollide(ship, ufoes, False):
            if shield == False:
                ship.health -= 1
                if long > 0:
                    long -= 0.5
                if red < 225 and green > 0:
                    red += 1
                    green -= 1
                if ship.health == 0:
                    game = False

        if pg.sprite.spritecollide(ship, meteors, False):
            if shield == False:
                ship.health -= 1
                if long > 0:
                    long -= 0.5
                if red < 225 and green > 0:
                    red += 1
                    green -= 1
                if ship.health == 0:
                    game = False

        if pg.sprite.spritecollide(ship, shield_boosts, True):
            shield = True
            sh_b_agr = False

        if sh_b_count == 300:
            shield = False
            sh_b_agr = True
            sh_b_count = 0

        if shield:       
            sh_b_count += 1
            
        if pg.sprite.spritecollide(ship, speed_boosts, True):
            speed += 5
            s_b_agr = False

        if s_b_count == 300:
            speed = 5
            s_b_agr = True
            s_b_count = 0

        if s_b_agr == False:       
            s_b_count += 1

        if pg.sprite.spritecollide(ship, hp_boosts, True):
            if ship.health <= 100 :
                ship.health += 100
                long += 50
                red -= 100
                green += 100
            if ship.health > 100 or ship.health <= 200:
                ship.health = ship.health + (200 - ship.health)
                long = long + (100 - long)
                red = red - (225 - (225 - red))
                green = green + (225 - green)
                

        collies = pg.sprite.groupcollide(bullets, ufoes, True, True)
        for bullet, ufo in collies.items():
            Boom(ufo[0].rect.center, boom_sprites, booms)
            killpoint += 1
            if killpoint == 30:
                game = False
                win = True
            #boom_sound.play()

        if counter > 5:
            game = False
        
        set_text(f'Пропущена: {counter}', 20, 20)
        set_text(f'Счёт: {killpoint}', 20, 45)
        
    else:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                play = False
        if win:
            mw.blit(fon_win, (0, 0))
        else:
            mw.blit(fon_go, (0, 0))

    pg.display.update()
    clock.tick(60)
    ticks += 1
from pygame import *
from random import randint

bl2 = False
l = 1 
window = display.set_mode((700, 500))
display.set_caption("Пиу-Пиу")
background = transform.scale(image.load("galaxy.jpg"),(700, 500))

font.init()
font = font.Font(None, 40)
win = font.render("YOU WIN!", True, (255, 215, 0))
level = font.render("Level " + str(l), True, (255, 215, 0))
over = font.render("GAME OVER", True, (255, 215, 0))

boostlevel2 = font.render(" Нажми f, чтобы увеличить скорость передвежения ракеты. Нажми g, чтобы увеличить скорость пули. Нажми h, чтобы пули не ичезали при столкнвении с врагом.", bl2, (255, 215, 0))

mixer.init()

mixer.music.load("space.ogg")
mixer.music.play()
bullets = sprite.Group()

k = 0
i = 0

speedb = 15

class Baby(sprite.Sprite):
    def __init__ (self,player_image, player_x, player_y, player_speed, sizex, sizey):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (sizex, sizey))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x ,self.rect.y))


class Player(Baby):
    def run(self):
        knopka = key.get_pressed()
        if knopka[K_a] and self.rect.x > 5:
            self.rect.x = self.rect.x - self.speed

        if knopka[K_d] and self.rect.x < 628:
            self.rect.x = self.rect.x + self.speed
    def fire(self):
        bullet1 = Bullet("bullet.png", self.rect.centerx, self.rect.top, speedb, 20, 15)
        
        bullets.add(bullet1)
        

class Inoplanetane(Baby):
    def update(self):
        global k
        self.rect.y = self.rect.y + self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(50, 650)
        if self.rect.y >= 500:
            k += 1
    
class Bullet(Baby):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
    
    




monster1 = Inoplanetane("ufo.png", randint(35, 665), 0, randint(1,2), 65, 65 )
monster2 = Inoplanetane("ufo.png", randint(35, 665), 0, randint(1,2), 65, 65 )
monster3 = Inoplanetane("ufo.png", randint(35, 665), 0, randint(1,2), 65, 65 )
monster4 = Inoplanetane("ufo.png", randint(35, 665), 0, randint(1,2), 65, 65 )
#monster5 = Inoplanetane("ufo.png", randint(35, 665), 0, randint(1,2), 65, 65 )
#monster6 = Inoplanetane("ufo.png", randint(35, 665), 0, randint(1,2), 65, 65 )
#monster7 = Inoplanetane("ufo.png", randint(35, 665), 0, randint(1,2), 65, 65 )
#monster8 = Inoplanetane("ufo.png", randint(35, 665), 0, randint(1,2), 65, 65 )
#monster9 = Inoplanetane("ufo.png", randint(35, 665), 0, randint(1,2), 65, 65 )
#monster10 = Inoplanetane("ufo.png", randint(35, 665), 0, randint(1,2), 65, 65 )

monsters = sprite.Group()

monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
#monsters.add(monster5)
#monsters.add(monster6)
#monsters.add(monster7)
#monsters.add(monster8)
#monsters.add(monster9)
#monsters.add(monster10)


sprite1 = Player("rocket.png", 300, 425, 6, 65, 65)

j = 0
t = 250
waiting = 1

game = True
finish = False
while game:

    keysp = key.get_pressed()
        
    for e in event.get():
        if e.type == QUIT:
            game = False
        if keysp[K_SPACE]:
            sprite1.fire()
        

    if finish != True:
        
        
        if i >= 10:
            
            window.blit(win, (210, 250))
            #l += 1
            #window.blit(boostlevel2, (j, t))
            #print("fdfd")
            for e1 in event.get():
                if e1.type == KEYDOWN:
                    if e1.key == K_f:
                        print(i,waiting)
                        sprite1 = Player("rocket.png", 300, 425, 8, 65, 65)
                        j = 2355
                        t = 0
                        display.update()
                    elif e1.key == K_g:
                        speedb += 5
                        j = 2355
                        t = 0
                    elif e1.key == K_g:
                        j = 2355
                        t = 0
                        if sprite.groupcollide(monsters, bullets, True, False):
                            i += 1
                
                            monsternew = Inoplanetane("ufo.png", randint(35, 665), 0, randint(1,5), 65, 65 )
                            monsters.add(monsternew)
        
                
        else:
                    
         
            window.blit(background, (0,0))
            sprite1.reset()
            sprite1.run()
            monsters.draw(window)
            monsters.update()
            bullets.update()
            bullets.draw(window)
            if k >= 5:
                
                window.blit(over, (210, 250))
                game = False
                
            if sprite.groupcollide(monsters, bullets, True, True) and l == 1:
                i += 1
            
                monsternew = Inoplanetane("ufo.png", randint(35, 665), 0, randint(1,5), 65, 65 )
                monsters.add(monsternew)
            
            schenchikw = font.render("Убито - " + str(i), True, (255, 0, 0))
            window.blit(schenchikw, (0, 0))
            schenchiko = font.render("Пропущено - " + str(k), True, (255, 0, 0))
            window.blit(schenchiko, (0, 40))
            window.blit(level, (0, 80))
            display.update()
            print(i,waiting)  


        time.delay(35)
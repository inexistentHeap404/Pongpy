import pygame
import random
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
global winS, screen, font, run, sound
pygame.mixer.init()
run = False
winS = [1000, 500]
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode(winS, 0, 32)
font = pygame.font.Font("fonts/ARDESTINE.ttf", 35)
def gameOver():
    pygame.mixer.Channel(2).play(pygame.mixer.Sound("music/gameOver2.mp3"))
    hi = open("hiscore.txt", "r")
    score = hi.read()
    global ot
    ot = "GAME OVER    YOU SCORED   "
    if int(score) < int(txt):
        pygame.mixer.Channel(2).play(pygame.mixer.Sound("music/himusic.mp3"))
        nf = open("hiscore.txt", "w")
        nf.write(str(int(txt)))
        nf.close()
        ot = "GAME OVER    NEW HIGH SCORE    YOU SCORED    "
    hi.close()
    oText = font.render(ot, True, (255, 255, 255), (0,0,0))
    oRect = oText.get_rect()
    oRect.center = ((screen.get_width() // 2) - 20, 400)
    screen.fill((0,0,0))
    otext = font.render(ot + str(int(txt)), True, (255, 255, 255), (0,0,0))
    screen.blit(otext, oRect)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pygame.quit()
        pygame.display.flip()
def setup():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("music/bgm3.mp3"), 1000)
    tup = True
    a = 0
    while True:
        wt = "PONG |   *  | PRESS SPACE TO PLAY"
        welText = font.render(wt, True, (255, 255, 255), (0,0,0))
        welRect = welText.get_rect()
        welRect.center = ((screen.get_width() // 2) - 20, ((screen.get_height() // 2)))
        if tup:
            wtext = font.render(wt, True, (0, 0, a), (0,0,0))
            a += 1
            screen.blit(wtext, welRect)
            if a == 255:
                tup = False
        if not tup:
            wtext = font.render(wt, True, (0, 0, a), (0,0,0))
            a -= 1
            screen.blit(wtext, welRect)
            if a == 0:
                tup = True
            
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    game()
        pygame.display.flip()
def game():
    run = True
    lwlloc = [0, 250]
    rwlloc = [990, 250]
    blloc = [10, 100]
    bspeed = [9, 3]
    lw = pygame.Rect(lwlloc, [10, 100])
    rw = pygame.Rect(rwlloc, [10, 100])
    pw = pygame.Rect([screen.get_width() / 2, 0], [1, 900])
    lu = False
    ru = False
    ld = False
    rd = False
    ball = pygame.draw.circle(screen, (255, 255, 255), [random.randint(0, 100), random.randint(30, 130)], 10)
    global txt
    txt = 0
    text = font.render(str(txt), True, (255,255,255), (0,0,0))
    trect = text.get_rect()
    trect.center = ((screen.get_width() // 2) - 20, 20)
    speed = 5
    lwe = pygame.Rect([lw.x, lw.y], [10, 100])
    rwe = pygame.Rect([rw.x, rw.y], [20, 100])
    c = 0
    cup = True
    run = False
    while True:
        lwe.x = lw.x
        rwe.x = rw.x
        lwe.y = lw.y
        rwe.y = rw.y
        if cup:
            c += 1
            screen.fill((0,0,c))
            if c == 255:
                cup = False
        if not cup:
            c -= 1
            screen.fill((0,0,c))
            if c == 0:
                cup = True
        blloc[0] += bspeed[0]
        blloc[1] += bspeed[1]
        pygame.draw.rect(screen, (255, 255, 255), lw)
        pygame.draw.rect(screen, (255, 255, 255), rw)
        pygame.draw.rect(screen, (50, 50, 50), pw)
        pygame.draw.circle(screen, (255, 255, 255), ball.center, 10)
        ball = ball.move(bspeed[0], bspeed[1])
        text = font.render(str(int(txt)), True, (255,255,255), (0,0,c))
        screen.blit(text, trect)
        if ball.colliderect(pw):
            txt += 0.5
            text = font.render(str(int(txt)), True, (0, 0, 0), (0, 0, c))
            trect = text.get_rect()
            trect.center = (screen.get_width() // 2, 20)
        if ru and rw.y > 0:
            rw.y -= speed
        if rd and rw.y < screen.get_height() - 100:
            rw.y += speed
        if lu and lw.y > 0:
            lw.y -= speed
        if ld and lw.y < screen.get_height() - 100:
            lw.y += speed
        if ball.colliderect(lw) or ball.colliderect(rw):
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("music/bounce3.wav"))
            bspeed[0] += 0.05 if bspeed[0] > 0 else -0.5
            bspeed[0] = -bspeed[0]
            if ball.colliderect(lw):
                pygame.draw.rect(screen, (0, 255, 0), lwe)
            else:
                pygame.draw.rect(screen, (0, 255, 0), rwe)
        if ball.top < 0 or ball.bottom > screen.get_height():
            bspeed[1] = -bspeed[1]
        if ball.left < -10 or ball.right > screen.get_width() + 10:
            pygame.mixer.Channel(0).pause()
            gameOver()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_w:
                    lu = True
                if event.key == K_s:
                    ld = True
                if event.key == K_UP:
                    ru = True
                if event.key == K_DOWN:
                    rd = True
            if event.type == KEYUP:
                if event.key == K_w:
                    lu = False
                if event.key == K_s:
                    ld = False
                if event.key == K_UP:
                    ru = False
                if event.key == K_DOWN:
                    rd = False
        pw.width = 1
        speed += 0.001
        clock.tick(60)
        pygame.display.flip()
setup()

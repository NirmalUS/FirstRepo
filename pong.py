import pygame
from pygame.locals import*
import random

pygame.init()
screen=pygame.display.set_mode((400,600))
green_colour=(5,255,15)

play1_score=0
play2_score=0

clock=pygame.time.Clock()

masterun=True
run=True
while masterun:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            masterun=False

        if event.type==pygame.KEYDOWN:
            if event.key==K_m:
                run=True

    ball_x=200
    ball_y=300
    ball_x_acc=round(random.uniform(-1.7,1.7),2)
    ball_y_acc=random.choice((1,-1))*1.3

    play1_x=200
    play1_y=20
    play1_acc=1
    play1_right=False
    play1_left=False
      
    play2_x=200
    play2_y=580
    play2_acc=1
    play2_right=False
    play2_left=False

    while run:
        screen.fill((10,10,10))
        clock.tick(120)

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==K_d:
                    play1_right=True
                elif event.key==K_s:
                    play1_left=True

                if event.key==K_l:
                    play2_right=True
                elif event.key==K_k:
                    play2_left=True

            if event.type==pygame.KEYUP:
                if event.key==K_d:
                    play1_right=False
                elif event.key==K_s:
                    play1_left=False

                if event.key==K_l:
                    play2_right=False
                elif event.key==K_k:
                    play2_left=False

        if ball_x>=390 or ball_x<=10:
            ball_x_acc=-ball_x_acc
        if play1_right:
            play1_x+=play1_acc
        elif play1_left:
            play1_x-=play1_acc
        if play2_right:
            play2_x+=play2_acc
        elif play2_left:
            play2_x-=play2_acc

        if play1_x<=30:
            play1_x=30
        elif play1_x>=370:
            play1_x=370

        if play2_x<=30:
            play2_x=30
        elif play2_x>=370:
            play2_x=370

        if ball_y<-10:
            play2_score+=1
            run=False
        elif ball_y>=610:
            play1_score+=1
            run=False

        ball_x+=ball_x_acc
        ball_y+=ball_y_acc
        ball=pygame.Rect(ball_x-4,ball_y-4,8,8)
        play1=pygame.Rect(play1_x-25,play1_y-5,50,10)
        play2=pygame.Rect(play2_x-25,play2_y-5,50,10)

        if pygame.Rect.colliderect(ball,play1) or pygame.Rect.colliderect(ball,play2):
            ball_y_acc=-ball_y_acc

        pygame.draw.rect(screen,green_colour,ball)
        pygame.draw.rect(screen,green_colour,play1)
        pygame.draw.rect(screen,green_colour,play2)
        pygame.display.update()
    print(play1_score,play2_score)
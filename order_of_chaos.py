import pygame
import random
import math
from pygame import mixer
pygame.init()
display = pygame.display.set_mode((1500,800))
#background music 

pygame.display.set_caption("Order of chaos")

ico = pygame.image.load('icons8-bug-32.png')

pygame.display.set_icon(ico)
playerimg = pygame.image.load('monster.png')
X = 750
Y = 720
X_change = 0
Y_change = 0

#enemy
enemyimg = []
X_ene = []
Y_ene = []
X_change_ene = []
Y_change_ene = []
num_of_ene = 5
for i in range(num_of_ene):
    enemyimg.append(pygame.image.load('sea-monster.png'))
    X_ene.append(random.randint(50,1500))
    Y_ene.append(random.randint(10,500))
    X_change_ene.append(0.3)
    Y_change_ene.append(40)

#bullet
bulletimg = pygame.image.load('f.png')
X_fire = 0
Y_fire = 720
X_change_fire = 0
Y_change_fire = 2
bull_state = "ready" # ready state you can't see the fire in ready state

#score
score_val = 0
font = pygame.font.Font('freesansbold.ttf',32)
X_score = 1330
Y_score = 10
over = pygame.font.Font('freesansbold.ttf',64)
#functions
def game_over():
    over_text = over.render("GAME OVER!",True,(255,255,255))
    display.blit(over_text,(650,400))
def points(x,y):
    points = font.render('score : '+str(score_val),True,(255,255,255))
    display.blit(points,(x,y))

def player(x,y):
    display.blit(playerimg,(x,y))

def enemy(x,y,i):
    display.blit(enemyimg[i],(x,y))

def splash(x,y):
    global bull_state 
    bull_state = "fire"
    display.blit(bulletimg,(x+16,y+10))

def collision(X_ene,Y_ene,X_fire,Y_fire):
    d = math.sqrt(math.pow(X_ene-X_fire,2)+math.pow(Y_ene-Y_fire,2))
    if d<35:
        return True
    else:
        return False

open = True
while open:
     #rgb for background
     display.fill((0,0,0))
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             open=False
     #if key stroke is pressed check -> or <-
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT:
                 X_change = 0.9
             elif event.key == pygame.K_LEFT:
                 X_change = -0.9
             elif event.key == pygame.K_SPACE:
                 if bull_state is "ready":
                     X_fire = X
                     splash(X_fire,Y_fire)
         if event.type == pygame.KEYUP:
             if event.type == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 X_change = 0
     # boundaries restriction
     X += X_change   

     if X<=0:
         X=0
     elif X>=1436:
         X = 1436
    #enemy boundaries    
     for i in range(num_of_ene):
         #game over
         if Y_ene[i] > 700:
             for j in range(num_of_ene):
                 Y_ene[j] = 2000
             game_over()
             break    
                 
         X_ene[i] += X_change_ene[i]
         if X_ene[i]<=0:
             X_change_ene[i]=0.3
             Y_ene[i] += Y_change_ene[i]
         elif X_ene[i]>=1372:
             X_change_ene[i] = -0.3
             Y_ene[i] += Y_change_ene[i]
         collide = collision(X_ene[i],Y_ene[i],X_fire,Y_fire)
         if collide:
            Y_fire = 720
            bull_state = "ready"
            score_val += 1
            X_ene[i] = random.randint(50,1378)
            Y_ene[i] = random.randint(10,450)

         enemy(X_ene[i],Y_ene[i],i)
    # bullet movement
     if Y_fire <=0:
         Y_fire = 720
         bull_state = "ready"
     if bull_state is "fire":
         splash(X_fire,Y_fire)
         Y_fire -= Y_change_fire

     
     player(X,Y)
     points(X_score,Y_score)
     pygame.display.update()

    

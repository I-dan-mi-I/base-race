import pygame, sys, math, time
from pygame.locals import *

pygame.init()

bg = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

ww = 1440
wh = 880

game_window = pygame.display.set_mode((ww, wh))
pygame.display.set_caption("AI RACE")

section = []
exec("section.append(pygame.image.load('track.png'))")

track = (100, 100, 100, 255)
fence  = (255, 5, 5, 255)

counter = 0

car = pygame.Rect(100, 165, 20, 20)
car_image = pygame.image.load("car.png")

explosion = pygame.image.load("explosion.png")


key_press_ = "false"
key_press__l = "false"
key_press__r = "false"
key_press__b = "false"

bew_counter_1 = 0
angel_1 = 0
destroy_1 = 0
count_destr_1 = 0

mvsp = 10
angel_ch = 4 / 8 

clock = pygame.time.Clock()
fps = 50
time_ = 0

running = True
while running:
    if count_destr_1 == 1:
        car.left = 100
        car.top = 165

    if count_destr_1 == 0:

        if key_press_ == "true" and bew_counter_1 < mvsp:
            bew_counter_1 += 0.25
        if key_press__b == "true":
            bew_counter_1 -= 0.25

        if key_press__l == "true" and bew_counter_1 > 2:
            angel_1 -= angel_ch * bew_counter_1
        elif key_press__l == "true" and bew_counter_1 < -2:
            angel_1 -= angel_ch * bew_counter_1
        
        if key_press__r == "true" and bew_counter_1 > 2:
            angel_1 += angel_ch * bew_counter_1
        elif key_press__r == "true" and bew_counter_1 < -2:
            angel_1 += angel_ch * bew_counter_1

        if key_press_ == "false" and bew_counter_1 > 0:
            bew_counter_1 -= 0.25
        if key_press__b == "false" and bew_counter_1 < 0:
            bew_counter_1 += 0.25

        b_1 = math.cos(math.radians(angel_1)) * bew_counter_1
        a_1 = math.sin(math.radians(angel_1)) * bew_counter_1
        car.left += round(b_1)
        car.top += round(a_1)

        car_image_neu = pygame.transform.rotate(car_image, angel_1*-1)

    else:
        count_destr_1 -= 1

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running =  False

            if event.key == K_RETURN:
                counter += 1
                car.left = 100
                car.top = 165
                angel_1 = 0
                
                if counter >= len(section):
                    counter = 0                    

            if event.key == K_w:
                key_press_ = "true"
            if event.key == K_a:
                key_press__l = "true"
            if event.key == K_d:
                key_press__r = "true"
            if event.key == K_s:
                key_press__b = "true"

        if event.type == KEYUP:
            if event.key == K_w:
                key_press_ = "false"
            if event.key == K_a:
                key_press__l = "false"
            if event.key == K_d:
                key_press__r = "false"
            if event.key == K_s:
                key_press__b = "false"

    game_window.fill((0, 0, 0))
    game_window.blit(section[counter], (0, 0))

    if count_destr_1 == 0:
        try:
            if not game_window.get_at((car.left + 10, car.top + 10)) == track:
                destroy_1 = 1

        except:
            destroy = 1

        if destroy_1 == 0:
            game_window.blit(car_image_neu, car)

    else:
        game_window.blit(explosion, car)

    if destroy_1 == 1:
        game_window.blit(explosion, car)
        pygame.display.update()
        bew_counter_1 = 0
        angel_1 = 0
        destroy_1 = 0
        count_destr_1 = 25

    pygame.display.update()

    clock.tick(fps)

pygame.quit()

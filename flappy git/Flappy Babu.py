import random
import pygame
import sys
import time


pygame.init()
clock = pygame.time.Clock()
clock2 = pygame.time.Clock()
screen_width = 900              #screen_width = 900  screen_height = 650
screen_height = 650

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Babu')
screen.fill(pygame.Color(25, 25, 25))

cloud1_size = random. choice((90, 100))
cloud2_size = random. choice((90, 100))


bird1 = pygame.image.load('Graphics/Bird anim 1.png')           #change
bird2 = pygame.image.load('Graphics/Bird anim 2.png')
bird1_c = pygame.image.load('Graphics/cird_c_1.png')           #change
bird2_c = pygame.image.load('Graphics/cird_c_2.png')

cloud1 = pygame.image.load('Graphics/Cloud.png')
cloud2 = pygame.image.load('Graphics/Cloud.png')

cloud1 = pygame.transform.scale(cloud1, (cloud1_size, cloud1_size))
cloud2 = pygame.transform.scale(cloud2, (cloud2_size, cloud2_size))

pipe_b = pygame.image.load('Graphics/Pipe1.png')              #change
pipe_t = pygame.image.load('Graphics/Pipe1.png')

bird1 = pygame.transform.scale(bird1, (50, 50))
bird2 = pygame.transform.scale(bird2, (50, 50))  #suposed to be 40
#For color
pipe_b_c=pygame.image.load('Graphics/Colored pipe.png').convert_alpha()
pipe_t_c=pygame.image.load('Graphics/Colored pipe.png').convert_alpha()
background = pygame.image.load('Graphics/eiolet.png').convert_alpha()
cloud1_c = pygame.image.load('Graphics/Cloud white.png').convert_alpha()
cloud2_c = pygame.image.load('Graphics/Cloud white.png').convert_alpha()
cloud1_c = pygame.transform.scale(cloud1_c, (cloud1_size, cloud1_size))
cloud2_c = pygame.transform.scale(cloud2_c, (cloud2_size, cloud2_size))

bird = bird1

pipe_b = pygame.transform.scale(pipe_b, (471, 470))
pipe_t = pygame.transform.scale(pipe_t, (471, 470))
pipe_t = pygame.transform.rotate(pipe_t, 181)






bird_x =60
bird2_x =60
bird_y= screen_height-400
bird2_y= -50
cloud1_x = screen_width+ screen_width/2
cloud1_y = screen_height/2 + random.randint(0,100)
cloud2_x = screen_width
cloud2_y = screen_height/2 + random.randint(0,100)
pipe_b_x= screen_width+40
pipe_b_y = random.randint(200,600)    #250
pipe_t_x = screen_width + 40
pipe_t_y = pipe_b_y - 630



#game comps
fly_sound = pygame.mixer.Sound("Sounds/wing.wav")
fly_sound.set_volume(0.3)
hit_sound = pygame.mixer.Sound("Sounds/die.wav")
hit_sound.set_volume(0.3)
death_sound = pygame.mixer.Sound("Sounds/die.wav")
death_sound.set_volume(0.3)
point_sound = pygame.mixer.Sound("Sounds/point.wav")
point_sound.set_volume(0.3)




#Variables
framerate= 60
bg_color= (25,25,25)
light_grey= (251,251,251)
g=1
b_s_c = 0
jumb=1
jumb_i=1
jumb_anim=0
bird_constant_speed=0
reset=0
i_bird_const_dis = 19                   #15
i_bird_const_speed= 9                  #10
i_bird = i_bird_const_dis          # /= smooth          i bird= distance
bg_anim=1
font_size = 80        #120
end_color= (255,0,0)
title=0
lost=0
font_i= 0
font_x=0
player_score =0
fly_sound_play = 0
hit_sound_play = 0
death_sound_play = 0
point_sound_play = 0
enter_size = 25
sub = 2
wing_i = 1
wing_anim = 0
pipe_speed = 5
bg=0
clr_change=0



#Functions
def gameover():
    global reset
    reset = 1



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and reset ==0:
                fly_sound_play += 1
                g = 0
                jumb = 1
                

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("yo")
                pipe_b=pipe_b_c
                pipe_t=pipe_t_c
                bg=1
                clr_change =1





    #for jumb animation
    if jumb_anim == 1:
        sub = 2
        i_bird -= i_bird/i_bird_const_speed
        #print(i_bird)
        bird_y -= i_bird
        



           #bird_y -= 4


    #when gravity is turned on
    if g==1:
        sub += sub /16
        bird_y += sub               #bird_y/25


        if bird_y < screen_height:   #above screen bottom
            bird_constant_speed = 1


    #if lost
    if bird_y < 0 or bird_y >= screen_height or lost == 1:
        bird_constant_speed = 0
        b_s_c = 0
        g = 0
        jumb = 0
        jumb_i = 1
        jumb_anim = 0
        reset = 1
        bg_anim=0
        gameover()
        title = 1
        sub = 2

    if bird_y < 0 or bird_y >= screen_height:
        death_sound_play += 1



    if reset == 1:

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                bird_y = screen_height / 2
                bg_anim = 1
                g = 1
                reset = 0  # -600)
                title = 0
                font_i = 0
                font_x = 0
                font_size = 80
                player_score = 0
                lost = 0
                pipe_b_x = screen_width - 160
                pipe_t_x = screen_width - 160
                pipe_b_y = random.randint(200, 550)
                pipe_t_y = pipe_b_y - 630
                hit_sound_play = 0
                death_sound_play = 0
                point_sound_play = 0
                sub = 2
                pipe_speed = 5
                





    #cloud
    if bg_anim==1:

        cloud1_x -= 3
        if cloud1_x <= -80:
            cloud1_size = random.randint(60, 150)
            cloud1 = pygame.transform.scale(cloud1, (cloud1_size, cloud1_size))
            cloud1_x = screen_width
            cloud1_y= random.randint(100,400)
        cloud2_x -= 3
        if cloud2_x <= -80:
            cloud2_size = random.randint(60, 150)
            cloud2 = pygame.transform.scale(cloud1, (cloud2_size, cloud2_size))
            cloud2_x = screen_width
            cloud2_y = random.randint(0, 500)


    #pipe
    if bg_anim == 1:
        pipe_b_x -= pipe_speed
        pipe_t_x -= pipe_speed
        if pipe_b_x <= -250:
            pipe_b_x= screen_width - 160
            pipe_t_x = screen_width - 160
            pipe_b_y = random.randint(200,550)
            pipe_t_y = pipe_b_y - 630             #580
            player_score += 1
            point_sound_play = 0

        if pipe_b_x <= -220:
            point_sound_play += 1



        #colision
    if bird_x >= pipe_b_x + 160:
        if  bird_x <= pipe_b_x + 260:       #x axis       #change    #160

            if bird_y < pipe_t_y + 460:        #470
                lost = 1
                hit_sound_play += 1
            if bird_y > pipe_b_y - 35:  # bottom
                lost=1
                hit_sound_play += 1




    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LALT:
            player_score += 1


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            g=1



    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP or  event.key == pygame.K_SPACE:
            fly_sound_play += 1
            g=0
            jumb = 1   #jumb=1   jumb_i=1   jumb_anim=0
            



    if jumb ==1:
        jumb_anim=1
        jumb_i+=1
        


    if jumb_i >= 33:
        jumb=0
        jumb_anim = 0
        g = 1
        fly_sound_play = 0

        i_bird = i_bird_const_dis
        jumb_i= 1


    #Sounds
    if fly_sound_play == 1:
        fly_sound.play()
        fly_sound_play += 1

    if hit_sound_play == 1:
        hit_sound.play()
        hit_sound_play += 1

    if death_sound_play == 1:
        death_sound.play()
        death_sound_play += 1

    if point_sound_play == 1:
        point_sound.play()
        point_sound_play += 1


    #wing animation
    wing_i+=1
    if wing_i % 5 ==0:
        wing_anim +=1



    if wing_anim %2 ==0:
        bird = bird2

    if wing_anim % 2 != 0:
        bird = bird1

    if bg==1:
        screen.blit(background, (0,0))
        
    if bg == 0:
        screen.fill(pygame.Color(25, 25, 25))
    if clr_change==1:
        pipe_b = pygame.transform.scale(pipe_b, (470, 470))
        pipe_t = pygame.transform.scale(pipe_t, (470, 470))
        pipe_t = pygame.transform.rotate(pipe_t, 180)
        print("brah")
        bird1= bird1_c
        bird2= bird2_c
        cloud1= cloud1_c
        cloud2= cloud2_c
        clr_change=0
    #Objects

    screen.blit(cloud1, (cloud1_x, cloud1_y))
    screen.blit(cloud2, (cloud2_x, cloud2_y))
    screen.blit(cloud1, (cloud1_x, cloud1_y))
    screen.blit(cloud2, (cloud2_x, cloud2_y))
    screen.blit(bird, (bird_x, bird_y))
    screen.blit(bird2, (bird2_x, bird2_y))
    screen.blit(pipe_b, (pipe_b_x, pipe_b_y))
    screen.blit(pipe_t, (pipe_t_x, pipe_t_y))
    gameover_font = pygame.font.Font("freesansbold.ttf", font_size)
    press_enter_font = pygame.font.Font("freesansbold.ttf", enter_size)  #
    score_font = pygame.font.Font("freesansbold.ttf", 50)
    game_over = gameover_font.render(f"GAME OVER", False, end_color)
    press_enter = press_enter_font.render(f"Press SPACE To Play Again", False, end_color)
    player_board = score_font.render(f"{player_score}", False, light_grey)


    if title==1:
        if font_i <= 30:
            font_size += 2
            font_x +=5
            font_i +=1
        screen.blit(game_over, (screen_width/2- 280 - font_x, screen_height/2 -  50 ))
        screen.blit(press_enter, (screen_width / 2 - 150 , screen_height / 2 + 100))
    screen.blit(player_board, (screen_width / 2 -15, 50))

    pygame.display.update()
    clock.tick(60)

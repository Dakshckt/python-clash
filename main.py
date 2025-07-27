import pygame
import constants
from constants import COMPLETED_STAGE1 , COMPLETED_STAGE2 , COMPLETED_STAGE3 , restart 
from stage1 import coverBackgroundStage1
from stage2 import coverBackgroundStage2
from stage3 import coverBackgroundStage3
from font import load_font , draw_text

pygame.init()
pygame.mixer.init()

WIN = pygame.display.set_mode((constants.EXTRA_WIDTH , constants.HEIGHT))
pygame.display.set_caption("Python Clash")

player_position_X =  (constants.WIDTH - constants.PLAYER_WIDTH) // 2  
player_position_Y = (constants.HEIGHT - constants.PLAYER_HEIGHT) // 1.5
direction = "Front"
is_moving = False
inx = 0
player_inx = 0
quit_game = False


player_images_front = [
    pygame.image.load("./Assets/Girl/images/f1.png"),
    pygame.image.load("./Assets/Girl/images/f2.png"),
    pygame.image.load("./Assets/Girl/images/f3.png"),
    pygame.image.load("./Assets/Girl/images/f4.png"),
]
player_images_back = [
    pygame.image.load("./Assets/Girl/images/b1.png"),
    pygame.image.load("./Assets/Girl/images/b2.png"),
    pygame.image.load("./Assets/Girl/images/b3.png"),
    pygame.image.load("./Assets/Girl/images/b4.png"),
]
player_images_left = [
    pygame.image.load("./Assets/Girl/images/l1.png"),
    pygame.image.load("./Assets/Girl/images/l2.png"),
    pygame.image.load("./Assets/Girl/images/l3.png"),
    pygame.image.load("./Assets/Girl/images/l4.png"),
]
player_images_right = [
    pygame.image.load("./Assets/Girl/images/r1.png"),
    pygame.image.load("./Assets/Girl/images/r2.png"),
    pygame.image.load("./Assets/Girl/images/r3.png"),
    pygame.image.load("./Assets/Girl/images/r4.png"),
]

def playerDisplay():
    global inx
    if direction == "Front":
        if is_moving:
            inx += 1
            if inx == 4:
                inx = 0 
            player_image = pygame.transform.scale(player_images_front[inx] , (constants.PLAYER_WIDTH , constants.PLAYER_HEIGHT))
        else:
            player_image = pygame.transform.scale(player_images_front[0] , (constants.PLAYER_WIDTH , constants.PLAYER_HEIGHT))

    elif direction == "Back":
        if is_moving:
            inx += 1
            if inx == 4:
                inx = 0 
            player_image = pygame.transform.scale(player_images_back[inx] , (constants.PLAYER_WIDTH , constants.PLAYER_HEIGHT))
        else:
            player_image = pygame.transform.scale(player_images_back[0] , (constants.PLAYER_WIDTH , constants.PLAYER_HEIGHT))

    elif direction == "Left":
        if is_moving:
            inx += 1
            if inx == 4:
                inx = 0 
            player_image = pygame.transform.scale(player_images_left[inx] , (constants.PLAYER_WIDTH , constants.PLAYER_HEIGHT))
        else:
            player_image = pygame.transform.scale(player_images_left[0] , (constants.PLAYER_WIDTH , constants.PLAYER_HEIGHT))

    elif direction == "Right":
        if is_moving:
            inx += 1
            if inx == 4:
                inx = 0 
            player_image = pygame.transform.scale(player_images_right[inx] , (constants.PLAYER_WIDTH , constants.PLAYER_HEIGHT))
        else:
            player_image = pygame.transform.scale(player_images_right[0] , (constants.PLAYER_WIDTH , constants.PLAYER_HEIGHT))

    WIN.blit(player_image , (player_position_X , player_position_Y))
    # pygame.draw.rect(WIN , (255 , 0 , 0) , (player_position_X , player_position_Y , constants.PLAYER_WIDTH , constants.PLAYER_HEIGHT) , 2)


def extraSpace():
    extraBackSteel = pygame.image.load("./Assets/tiles/Steel.png")
    extraBackSteel = pygame.transform.scale(extraBackSteel , (constants.BACKGROUND_BOX , constants.BACKGROUND_BOX))
    extraBackGray = pygame.image.load("./Assets/tiles/LightGrey.png")
    extraBackGray = pygame.transform.scale(extraBackGray , (constants.BACKGROUND_BOX , constants.BACKGROUND_BOX))
    for x in range(constants.WIDTH , constants.EXTRA_WIDTH , constants.BACKGROUND_BOX):
        for y in range(0 , constants.HEIGHT , constants.BACKGROUND_BOX):
            if y == 0 or x == constants.WIDTH:
                WIN.blit(extraBackSteel , (x , y))
            elif y >= constants.BACKGROUND_BOX and y < constants.BACKGROUND_BOX * 8:
                pygame.draw.rect(WIN , (255 , 255, 255) , (x , y , constants.BACKGROUND_BOX , constants.BACKGROUND_BOX))
                pygame.draw.rect(WIN , (235 , 235, 235) , (x , y , constants.BACKGROUND_BOX , constants.BACKGROUND_BOX) , 6)
                pygame.draw.rect(WIN , (200 , 200, 200) , (x , y , constants.BACKGROUND_BOX , constants.BACKGROUND_BOX) , 2)
            else:
                WIN.blit(extraBackGray , (x , y))
            

def background(keys , mouse_x , mouse_y , button_clicked):
    global player_position_X , player_position_Y , player_inx , direction , quit_game
    extraSpace()
    if constants.COMPLETED_STAGE1 == False:
        # print("The background 1 is priting")
        if player_inx == 0:
            direction = "Front"
            constants.BANNER_DISPLAY = True
            player_position_X =  (constants.WIDTH - constants.PLAYER_WIDTH) // 2  
            player_position_Y = (constants.HEIGHT - constants.PLAYER_HEIGHT) // 1.5
            pygame.mixer.music.stop()
            pygame.mixer.music.load("./Assets/Sound/pokemon_title_sond_track.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            player_inx += 1
        coverBackgroundStage1(WIN , player_position_X , player_position_Y , keys , mouse_x , mouse_y , button_clicked)
    elif constants.COMPLETED_STAGE2 == False:
        # print("The background 2 is priting")
        if player_inx == 1:
            direction = "Front"
            constants.BANNER_DISPLAY = True
            player_position_X =  (constants.WIDTH - constants.PLAYER_WIDTH) // 2  
            player_position_Y = (constants.HEIGHT - constants.PLAYER_HEIGHT) // 1.5
            pygame.mixer.music.stop()
            pygame.mixer.music.load("./Assets/Sound/pokemon_welcome_sond_track.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            player_inx += 1
        coverBackgroundStage2(WIN , player_position_X , player_position_Y , keys , mouse_x , mouse_y , button_clicked)
    elif constants.COMPLETED_STAGE3 == False:
        # print("The background 3 is priting")
        if player_inx == 2:
            direction = "Front"
            constants.BANNER_DISPLAY = True
            player_position_X =  (constants.WIDTH - constants.PLAYER_WIDTH) // 2  
            player_position_Y = (constants.HEIGHT - constants.PLAYER_HEIGHT) // 1.5
            pygame.mixer.music.stop()
            pygame.mixer.music.load("./Assets/Sound/pokemon_end_sound_track.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            player_inx += 1
        coverBackgroundStage3(WIN , player_position_X , player_position_Y , keys , mouse_x , mouse_y , button_clicked)
    else:
        constants.BANNER_DISPLAY = True
        direction = "Front"
        player_position_X =  (constants.WIDTH - constants.PLAYER_WIDTH) // 2  
        player_position_Y = (constants.HEIGHT - constants.PLAYER_HEIGHT) // 1.5
        player_inx = 0
        restart()

    if constants.REARRANGE_PLAYER_POSITION:
        direction = "Front"
        player_position_X =  (constants.WIDTH - constants.PLAYER_WIDTH) // 2  
        player_position_Y = (constants.HEIGHT - constants.PLAYER_HEIGHT) // 1.5
        constants.REARRANGE_PLAYER_POSITION = False
        constants.DISBALE_KEY = False

    quit_x = constants.WIDTH + (constants.BACKGROUND_BOX * 3)
    quit_y = constants.HEIGHT - (constants.BACKGROUND_BOX * 2)
    quitButton = pygame.image.load("./Assets/tiles/BrownButton.png")
    quitButton = pygame.transform.scale(quitButton , (constants.BACKGROUND_BOX * 2 , constants.BACKGROUND_BOX))
    WIN.blit(quitButton , (quit_x , quit_y))
    draw_text(WIN , "QUIT" , quit_x + 30 , quit_y + 20 , 1)
    quit_button = pygame.Rect(quit_x , quit_y , constants.BACKGROUND_BOX * 2 , constants.BACKGROUND_BOX)

    if mouse_x != None and mouse_y != None:
        if quit_button.collidepoint(mouse_x , mouse_y):
            quit_game = True

    if quit_game == True:
        constants.BANNER_DISPLAY = True
        direction = "Front"
        player_position_X =  (constants.WIDTH - constants.PLAYER_WIDTH) // 2  
        player_position_Y = (constants.HEIGHT - constants.PLAYER_HEIGHT) // 1.5
        player_inx = 0
        quit_game = False
        restart()

    playerDisplay()
    pygame.display.update()


def main():
    global player_position_X , player_position_Y , direction , is_moving
    clock = pygame.time.Clock()
    run = True

    load_font()

    button_clicked = pygame.mixer.Sound("./Assets/Sound/pokemon-a-button.mp3")
    button_clicked.set_volume(1)


    while run:
        clock.tick(constants.FPS)
        mouse_x = None
        mouse_y = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                button_clicked.play(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_clicked.play()
                    mouse_x , mouse_y = event.pos

        keys = pygame.key.get_pressed()
        is_moving = False

        if not constants.DISBALE_KEY:
            if keys[pygame.K_LEFT] and player_position_X > 0:
                constants.BANNER_DISPLAY = False
                player_position_X -= constants.STEP
                direction = "Left"
                is_moving = True
            elif keys[pygame.K_RIGHT] and player_position_X < constants.WIDTH - constants.PLAYER_WIDTH:
                constants.BANNER_DISPLAY = False
                player_position_X += constants.STEP
                direction = "Right"
                is_moving = True
            elif keys[pygame.K_UP] and player_position_Y > 0:
                constants.BANNER_DISPLAY = False
                player_position_Y -= constants.STEP
                direction = "Back"
                is_moving = True
            elif keys[pygame.K_DOWN] and player_position_Y < constants.HEIGHT - constants.PLAYER_HEIGHT:
                constants.BANNER_DISPLAY = False
                player_position_Y += constants.STEP
                direction = "Front"
                is_moving = True


        background(keys , mouse_x , mouse_y , button_clicked)
    
    pygame.quit()


if __name__ == "__main__":
    main()


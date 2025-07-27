import pygame
import constants
from constants import FONT , HEADING
from font import draw_text
import random
import database
from database import split_into_chunks , MCQ_STAGE_1
import tkinter as tk
from tkinter import messagebox
from exam import examForm

pygame.init()
pygame.mixer.init()

image = pygame.image.load("./Assets/tiles/blue.png")
image = pygame.transform.scale(image , (constants.BACKGROUND_BOX , constants.BACKGROUND_BOX))
gate_width = 100
gate_height = 20

inx = 0
five_question = []
questions_places = []

# ? Generating the Random values for the rect in the background
while len(questions_places) < 5:
    is_valid = True
    question_x = random.randrange(constants.PLAYER_WIDTH , constants.HEIGHT - constants.PLAYER_HEIGHT , constants.PLAYER_WIDTH)
    question_y = random.randrange(constants.PLAYER_WIDTH , constants.HEIGHT - constants.PLAYER_HEIGHT , constants.PLAYER_WIDTH)
    for val in questions_places:
        if question_x == val[0] and question_y == val[1]:
            is_valid = False
        elif question_x == val[0] + constants.BACKGROUND_BOX and question_y == val[1] + constants.BACKGROUND_BOX:
            is_valid = False
        elif question_x == val[0] - constants.BACKGROUND_BOX and question_y == val[1] - constants.BACKGROUND_BOX:
            is_valid = False
        elif question_x == val[0] - constants.BACKGROUND_BOX and question_y == val[1] + constants.BACKGROUND_BOX:
            is_valid = False
        elif question_x == val[0] + constants.BACKGROUND_BOX and question_y == val[1] - constants.BACKGROUND_BOX:
            is_valid = False
        elif question_x == val[0] and question_y == val[1] + constants.BACKGROUND_BOX:
            is_valid = False
        elif question_x == val[0] and question_y == val[1] - constants.BACKGROUND_BOX:
            is_valid = False
        elif question_x == val[0] - constants.BACKGROUND_BOX and question_y == val[1]:
            is_valid = False
        elif question_x == val[0] + constants.BACKGROUND_BOX and question_y == val[1]:
            is_valid = False

    if is_valid == False:
        continue

    questions_places.append([question_x , question_y])

data = []

# ? Printing the Rect Question on the maps 
for val in questions_places:
    question = database.LESSON_STAGE_1[inx]
    inx += 1
    rect = pygame.Rect(val[0] ,val[1] , constants.PLAYER_WIDTH , constants.PLAYER_HEIGHT)
    data.append((rect , question))
    


# ? Main Background Logic
def coverBackgroundStage1(WIN , player_position_x , player_position_y , keys , mouse_x , mouse_y , button_clicked):


    global inx , five_question
    for x in range(0 , constants.WIDTH , 50):
        for y in range(0 , constants.HEIGHT , 50):
            WIN.blit(image , (x , y))

    gate = pygame.draw.rect(WIN , (0 , 0 , 0) , ((constants.WIDTH - gate_width)//2 , 0 , gate_width , gate_height))

    for rect , database in data:
        pygame.draw.rect(WIN , (235 , 235 , 235) , rect , 6)
        pygame.draw.rect(WIN , (255, 234, 0) , rect , 4)
        pygame.draw.rect(WIN , (155, 134, 0) , rect , 1)


    if constants.BANNER_DISPLAY:
        banner = pygame.transform.scale(constants.BANNER_IMAGE , (constants.BANNER_WIDTH , constants.BANNER_HEIGHT))
        WIN.blit(banner , (constants.BANNER_CENTER_X , constants.BANNER_CENTER_Y))
        draw_text(WIN , "Stage One" , constants.BANNER_CENTER_X + 180 , constants.BANNER_CENTER_Y + 30 , 2)
        draw_text(WIN , "Five Question" , constants.BANNER_CENTER_X + 195 , constants.BANNER_CENTER_Y + 60 , 1)
        draw_text(WIN , "Move to any direction to Start the Game" , constants.BACKGROUND_BOX  , constants.HEIGHT - (constants.BACKGROUND_BOX * 5.8) , 1.5)
        python_image = pygame.image.load("./Assets/Logo/python.png")
        python_image = pygame.transform.scale(python_image , (50 , 50))
        WIN.blit(python_image , (8 , 8))
    else:
        draw_text(WIN , "Stage One" , 10 , 10 , 1.5)
        draw_text(WIN , "Five Question" , 18 , 30 , 0.8)

    text_surface = HEADING.render("Variables" , True , (0,0,0))
    WIN.blit(text_surface , (constants.WIDTH + constants.BACKGROUND_BOX + 10 , constants.BACKGROUND_BOX + 30 ))

    for rect , database in data:
        if rect.x == player_position_x and rect.y == player_position_y:
            draw_text(WIN , "Click )A to Get Description" , 100 , 100 , 2)
            if keys[pygame.K_a]:
                button_clicked.play()
                text_y = constants.BACKGROUND_BOX + 70
                result = split_into_chunks(database)
                for line in result:
                    text_surface = FONT.render(line , True , (0 , 0 , 0))
                    WIN.blit(text_surface , (constants.WIDTH + constants.BACKGROUND_BOX + 10 , text_y)) 
                    text_y += 20







    if player_position_y <= gate.y + gate.height and player_position_x + constants.PLAYER_WIDTH >= gate.x and player_position_x <= gate.x + gate.width:
        constants.DISBALE_KEY = True
        if not five_question:
            five_question = random.sample(MCQ_STAGE_1 , 5)
        if constants.EXAM_1 == False:
            examForm(WIN , five_question , mouse_x , mouse_y , "form1")

    if constants.EXAM_1 == True:
        constants.COMPLETED_STAGE1 = True
        constants.DISBALE_KEY = False


    inx = 0
    

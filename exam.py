import pygame
import constants
from constants import HEADING , FONT , restart
from database import split_into_chunks_10
from font import draw_text
import tkinter
from tkinter import messagebox

pygame.init()
pygame.mixer.init()

take_question = 0
question_no = 0
inx_values = [2 , 2.5 , 2.5 , 3 , 3.5 , 4]
test_one_result = []
ans_button = []



def checkResult(corrects , submitted):
    result = []
    for correct , submit in zip(corrects , submitted):
        if correct == submit:
            result.append(True)
        else:
            result.append(False)
            
    if False in result:
        return False
    else:
        return True


def redefined():   
    global question_no , inx_values , test_one_result , ans_button , take_question
    question_no = 0
    inx_values = [2 , 2.5 , 2.5 , 3 , 3.5 , 4]
    test_one_result = []
    ans_button = []
    take_question = 0


def Button(WIN , x , y , width , height):
    button_image = pygame.image.load("./Assets/tiles/RedButton.png")
    button_image = pygame.transform.scale(button_image , (width , height))
    WIN.blit(button_image , (x , y))
    return button_image.get_rect(topleft=(x , y))

def examForm(WIN , questions , mouse_x , mouse_y , form):
    global question_no , test_one_result , ans_button , take_question

    if take_question == 0:
        for question in questions:
            test_one_result.append(question["answer"])
        take_question += 1
    

    # ? Displaying the Board
    board = pygame.image.load("./Assets/tiles/beige.png")
    board = pygame.transform.scale(board , (constants.BACKGROUND_BOX , constants.BACKGROUND_BOX))
    for x in range(0 + constants.BACKGROUND_BOX , constants.WIDTH - constants.BACKGROUND_BOX , constants.BACKGROUND_BOX):
        for y in range(0 + constants.BACKGROUND_BOX , constants.HEIGHT - constants.BACKGROUND_BOX , constants.BACKGROUND_BOX):
            WIN.blit(board , (x , y))
    
    # ? Displaying the Question
    single_question = questions[question_no]
    result = split_into_chunks_10(single_question["question"])
    for inx , line in zip(inx_values , result):
        text_surface = FONT.render(line , True , (0,0,0))
        WIN.blit(text_surface , ((constants.BACKGROUND_BOX*2),(constants.BACKGROUND_BOX*inx))) 
    
    # ? Displaying the Options
    padding = 1
    options = single_question["options"]
    for option in options:
        result = split_into_chunks_10(option)
        for line in result:
            text_surface = FONT.render(line , True , (0,0,0))
            WIN.blit(text_surface , ((constants.BACKGROUND_BOX*2),(constants.BACKGROUND_BOX*(3.5+ padding))))
            padding += 1
    
    # ? Displaying Red Button
    buttons = {}
    for inx , val in enumerate(range(2 , 10 , 2)):
        x = (constants.BACKGROUND_BOX * val) + (inx * 25)
        buttons[f"button_{inx+1}"] = Button(WIN , x , constants.HEIGHT - (constants.BACKGROUND_BOX * 3) , constants.OPTION_BUTTON_WIDTH , constants.OPTION_BUTTON_HEIGHT)
    

    # ? Checking the Button Clicked is on which button
    if mouse_x != None or mouse_y != None:
        for button in buttons:
            # button_x = buttons[button].x
            # button_y = buttons[button].y
            # button_width = buttons[button].width
            # button_height = buttons[button].height

            # if button_x < mouse_x and button_y < mouse_y and mouse_x < button_x + button_width and mouse_y < button_y + button_height:
            if buttons[button].collidepoint(mouse_x, mouse_y):
                # print(button)
                if button == "button_1":
                    ans_button.append("(A)")
                elif button == "button_2":
                    ans_button.append("(B)")
                elif button == "button_3":
                    ans_button.append("(C)")
                elif button == "button_4":
                    ans_button.append("(D)")
                
                question_no += 1
            
    

    # ? Paper Checking is remaining 
    if len(ans_button) == 5:
        if form == "form1":
            # ? Should be Done Here <-
            result = checkResult(test_one_result , ans_button)
            if result == True:
                constants.EXAM_1 = True
                redefined()
            else:
                constants.REARRANGE_PLAYER_POSITION = True
                messagebox.showinfo("Information","You Got some of the answer Wrong")
                redefined()
        elif form == "form2":
            # ? Should be Done Here <-
            result = checkResult(test_one_result , ans_button)
            if result == True:
                constants.EXAM_2 = True
                redefined()
            else:
                constants.REARRANGE_PLAYER_POSITION = True
                messagebox.showinfo("Information","You Got some of the answer Wrong")
                redefined()
        elif form == "form3":
            # ? Should be Done Here <-
            result = checkResult(test_one_result , ans_button)
            if result == True:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("./Assets/Sound/pokemon_obtain_gym_badge.mp3")
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play()
                messagebox.showinfo("Information","User Won the Game")
                constants.EXAM_3 = True
                redefined()
            else:
                constants.REARRANGE_PLAYER_POSITION = True
                messagebox.showinfo("Information","You Got some of the answer Wrong")
                redefined()
            redefined()
        

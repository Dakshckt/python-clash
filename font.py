import pygame

CHAR_MAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,:?!()+-"

CHAR_WIDTH = 8
CHAR_HEIGHT = 10
FONT_ROWS = 6
FONT_COLUMNS = 10
spacing = 2

sprite_sheet = None

def load_font(): 
    global sprite_sheet      
    sprite_sheet = pygame.image.load("./Assets/Fonts/font.png").convert_alpha()


def get_character_image(char):
    char = char.upper()

    if char in CHAR_MAP:
        index = CHAR_MAP.index(char)

        col = index % FONT_COLUMNS
        row = index // FONT_COLUMNS
        x = col * CHAR_WIDTH
        y = row * CHAR_HEIGHT

        char_image = sprite_sheet.subsurface(pygame.Rect(x , y , CHAR_WIDTH , CHAR_HEIGHT))
        return char_image

    else:
        return None

def draw_text(surface , text , x , y , font_size):
    new_x = 0

    for char in text:
        char_image = get_character_image(char)
        if char_image:
            char_image = pygame.transform.scale(char_image , (CHAR_WIDTH * font_size , CHAR_HEIGHT * font_size))
            surface.blit(char_image , (x + new_x , y))
            new_x += (CHAR_WIDTH * font_size) + spacing
        else:
            new_x += (CHAR_WIDTH * font_size) + spacing 

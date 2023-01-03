import pygame
import os
import constants
import random

pygame.font.init()
pygame.init()

WIN = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Interval Game!")

POSSIBLE_NOTES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e_h', 'f_h']
NOTE_POSITIONS = {'e': 250, 'f': 225, 'g' : 200, 'a': 175, 'b' : 150, 'c': 125, 'd': 100, 'e_h': 75,'f_h': 50}

BACKGROUND = pygame.image.load(os.path.join('Assets', 'whiteScreen.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND, (constants.WIDTH, constants.HEIGHT))


def draw_pointer(note):
    pass

def draw_sheet():
    LINE1 = pygame.Rect(100, 200, 800, 5)
    LINE2 = pygame.Rect(100, 250, 800, 5)
    LINE3 = pygame.Rect(100, 300, 800, 5)
    LINE4 = pygame.Rect(100, 350, 800, 5)
    LINE5 = pygame.Rect(100, 400, 800, 5)
    VERTICAL1 = pygame.Rect(100, 200, 10, 200)
    VERTICAL2 = pygame.Rect(900, 200, 5, 205)
    
    pygame.draw.rect(WIN, constants.BLACK, LINE1)
    pygame.draw.rect(WIN, constants.BLACK, LINE2)
    pygame.draw.rect(WIN, constants.BLACK, LINE3)
    pygame.draw.rect(WIN, constants.BLACK, LINE4)
    pygame.draw.rect(WIN, constants.BLACK, LINE5)
    pygame.draw.rect(WIN, constants.BLACK, VERTICAL1)
    pygame.draw.rect(WIN, constants.BLACK, VERTICAL2)

def draw_player(image_num, pos):
    # the pos here is the y axis coordinate of the player
    # image_num is the index of the sprite animation image
    player_image = constants.image_sprite[image_num]
    player_image = pygame.transform.scale(player_image, (75, 75))
    positions = [150, 175, 200, 225, 250, 275, 300, 325, 350]       # the y positions of my player
    WIN.blit(player_image, (150, positions[pos]))      


def draw_notes(notes):   # takes in a list of positions
    QUARTERNOTE_IMAGE = pygame.image.load(os.path.join('Assets', 'Notes', 'QuarterNote.png'))
    QUARTERNOTE = pygame.transform.scale(QUARTERNOTE_IMAGE, (100,195))
    # EIGHTNOTE_IMAGE = pygame.image.load(os.path.join('Assets', 'Notes', 'EightNote.png'))
    # EIGHTNOTE = pygame.transform.scale(EIGHTNOTE_IMAGE, (80,185))
    # use 100, 150, 200, 250, or 300 in the y coordinate. you will land on the line
    # write the y coordinate in the format 100 +- 25 - 3. This will place the note in the center
    
    # for note in notes:
    #     WIN.blit(QUARTERNOTE, (pos[0], pos[1])) 
    WIN.blit(QUARTERNOTE, (260, NOTE_POSITIONS[notes[0]]))
    WIN.blit(QUARTERNOTE, (420, NOTE_POSITIONS[notes[1]]))
    WIN.blit(QUARTERNOTE, (580, NOTE_POSITIONS[notes[2]]))
    WIN.blit(QUARTERNOTE, (740, NOTE_POSITIONS[notes[3]]))

def draw_winner():
    draw_text = constants.WINNER_FONT.render('Level Passed!', 1, constants.RED)
    WIN.blit(draw_text, ((constants.WIDTH/2 - draw_text.get_width()/2), constants.HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)   
        
def draw_endgame():
    draw_text = constants.WINNER_FONT.render('You Lost', 1, constants.BLACK)
    WIN.blit(draw_text, ((constants.WIDTH/2 - draw_text.get_width()/2), constants.HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)   

def draw_window(position, image_num, y_player_pos):
    # pygame.draw.rect(WIN, constants.WHITE, background)
    # player_image = constants.image_sprite[image_num]
    # player_image = pygame.transform.scale(player_image, (100, 100))
    
    WIN.blit(BACKGROUND, (0, 0))
    draw_sheet()
    draw_notes(position)
    draw_player(image_num, y_player_pos)
    pygame.display.update()

def main():

    clock = pygame.time.Clock()
    run = True
    pointer = 0
    life = 3
    curr_key = ''
    y_player_pos = 0
    # success = False

    sequence = []
    notes = []
    for i in range(4):
        notes.append(random.choice(POSSIBLE_NOTES))

    image_num = 0 # for printing the sprite character

    draw_window(notes, image_num, y_player_pos)
    # print(notes)

    while run:
        clock.tick(constants.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                        curr_key = 'e'
                        if notes[pointer] == 'e':
                            sequence.append('e')
                            pointer += 1
                        
                
                elif event.key == pygame.K_f:
                        curr_key = 'f'
                        if  notes[pointer] == 'f':
                            sequence.append('f')
                            pointer += 1
                        
                    
                elif event.key == pygame.K_g  :
                        curr_key = 'g'
                        if notes[pointer] == 'g':
                            sequence.append('g')
                            pointer += 1
                        

                elif event.key == pygame.K_h  :
                        curr_key = 'a'
                        if notes[pointer] == 'a':
                            sequence.append('a')
                            pointer += 1
                        

                elif event.key == pygame.K_j  :
                        curr_key = 'b'
                        if notes[pointer] == 'b':
                            sequence.append('b')
                            pointer += 1
                        

                elif event.key == pygame.K_k:
                        curr_key = 'c'
                        if notes[pointer] == 'c':
                            sequence.append('c')
                            pointer += 1
                        

                elif event.key == pygame.K_l  :
                        curr_key = 'd'
                        if notes[pointer] == 'd':
                            pointer += 1
                            sequence.append('d')

                elif event.key == pygame.K_SEMICOLON:
                        curr_key = 'e_h'
                        if notes[pointer] == 'e_h':
                            sequence.append('e_h')
                            pointer += 1
                        

                elif event.key == pygame.K_QUOTE:
                        curr_key = 'f_h'
                        if notes[pointer] == 'f_h':
                            pointer += 1
                            sequence.append('f_h')
                else:
                    life -= 1

        # print(f'curr_key is {curr_key}')
        # print(f'notes are {notes}')
        # print(f'sequence is {sequence}')
        if image_num == 4:  # hard coded the 4 here
            image_num = 0

        if curr_key == '':
            y_player_pos = 0
        else:
            y_player_pos = constants.player_positions[curr_key]

        draw_window(notes, image_num, y_player_pos)     # image_num is for printing the sprite image
        image_num += 1
        
        pygame.display.update()

            # if event.type == RED_HIT:
            #     red_health -= 1
            #     BULLET_HIT_SOUND.play()

            # if event.type == YELLOW_HIT:
            #     yellow_health -= 1
            #     BULLET_HIT_SOUND.play()
        
        # print('sequence is', sequence)
        # print('notes are', notes)

        # if life == 0:
        #     draw_endgame()
        #     pointer = 0
        #     notes = []
        #     sequence = []
        #     for i in range(4):
        #         notes.append(random.choice(POSSIBLE_NOTES))

            # draw_window(notes)
        if sequence == notes:
            draw_winner()
            pointer = 0
            notes = []
            sequence = []
            for i in range(4):
                notes.append(random.choice(POSSIBLE_NOTES))

            draw_window(notes, 0, y_player_pos)
            # run = False

        
    # if success == False:
    #     print('run')
    #     pygame.time.delay(50000)

    pygame.quit()

if __name__ == '__main__':
    main()
#!/usr/bin/env python3

import pygame
import random


def who_goes_first():
    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"


def display_window():
    pygame.display.set_caption("Tic Tac Toe")
    return pygame.display.set_mode(SCREEN_SIZE)


def create_grid(GRID):

    for row in range(3):
        GRID.append([])
        for column in range(3):
            GRID[row].append('')

def token_indicator(COLOR, x, y, WIDTH, HEIGHT):
    pygame.draw.rect(SCREEN, COLOR, [x, y,  WIDTH, HEIGHT])
    

def indicator_color():
    if who_goes_first() == "Player 1":
        return  BLUE
    else:
        return  RED

def draw_board(SCREEN, white, margin, width, height, GRID, BLACK):
    SCREEN.fill(BLACK)
    for row in range(4):
        if row < 3:
            for column in range(3):
                COLOR = WHITE
                if GRID[row][column] == 'x':
                    COLOR = RED
                elif GRID[row][column] == 'o':
                    COLOR = BLUE

                pygame.draw.rect(SCREEN, COLOR, [
                                 (margin + width) * column + margin, (margin + height) * row + margin, width, height])

        else:
            pygame.draw.rect(SCREEN, WHITE, [
                             (margin), (margin + height) + 205, (295 - margin), (80 - margin)])
    


def button(SCREEN, text, x, y, WIDHT, height, COLOR, action=None):

    mouseX, mouseY = pygame.mouse.get_pos()
    press = pygame.mouse.get_pressed()

    if press[0]:
        # For debugging mouse pointer location and coordinates.
        print("coordinates: x + width = {}, mouseX = {}, x = {}\n".format(x + WIDHT, mouseX, x))
        print("coordinates: Y + height = {}, mouseY = {}, y = {}\n".format(y + height, mouseY, y))

    if x + WIDHT > mouseX < x and (not mouseY < 310 and not mouseY > 340):
        if press[0] and action != None:
            action()

    font = pygame.font.SysFont("comicsansms", 35)
    text = font.render(text, True, COLOR)
    box = text.get_rect()
    box.center = (x // 2, y // 2)
    SCREEN.blit(text, box)


def game_exit():
    pygame.quit()
    quit()


def check(GRID, content):
    return ((GRID[0][0] == content and GRID[0][1] == content and GRID[0][2] == content) or
            (GRID[1][0] == content and GRID[1][1] == content and GRID[1][2] == content) or
            (GRID[2][0] == content and GRID[2][1] == content and GRID[2][2] == content) or

            (GRID[0][0] == content and GRID[1][0] == content and GRID[2][0] == content) or
            (GRID[0][1] == content and GRID[1][1] == content and GRID[2][1] == content) or
            (GRID[0][2] == content and GRID[1][2] == content and GRID[2][2] == content) or

            (GRID[0][0] == content and GRID[1][1] == content and GRID[2][2] == content) or
            (GRID[2][0] == content and GRID[1][1] == content and GRID[0][2] == content))

def result(TEXT):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()

        SCREEN.fill(WHITE)
        label(SCREEN, TEXT, 40, 300, 250, 20, 20)
        button(SCREEN, "Play", 150, 650, 20, 20, BLUE, main)
        button(SCREEN, "Quit", 450, 650, 20, 20, RED, game_exit)
        pygame.display.flip()

def main():
    GRID = []
    SCORE = 0
    TURN = who_goes_first()
    INDI = indicator_color()
    
    create_grid(GRID)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                print("Pressed: {}, Grid coordinates: row: {}, column: {}".format(pos, row, column))
                
                
                if TURN == "Player 1" and (row != 3 and row != 4 and row != 5):
                    if GRID[row][column] == '':
                        content = 'x'
                        GRID[row][column] = 'x'
                        INDI = BLUE
                        
                        

                        if check(GRID, content):
                            SCORE += 1
                           
                            result("Player 1 Wins!")
                            print('Player 1 wins')

                        else:
                            if '' not in GRID[0] and '' not in GRID[1] and '' not in GRID[2]:
                                result("Draw!")
                                print('draw')

                            else:
                                TURN = "Player 2"

                elif TURN == "Player 2" and (row != 3 and row != 4 and row != 5 and column != 3):
                    if GRID[row][column] == '':
                        content = 'o'
                        GRID[row][column] = 'o'
                        INDI = RED
                        
                   
                        if check(GRID, content):
                            SCORE += 1
                           
                            result("Player 2 Wins!")
                            print('Player 2 wins')

                        else:

                            if '' not in GRID[0] and '' not in GRID[1] and '' not in GRID[2]:
                                result("Draw!")

                            else:
                                TURN = "Player 1"

        SCREEN.fill(BLACK)
        draw_board(SCREEN, WHITE, MARGIN, WIDTH, HEIGHT, GRID, BLACK)
        label(SCREEN, "Turn: " + TURN, 35, 200, 680, 20, 20)
        token_indicator(INDI, 200, 310, 80, 60)
        pygame.display.flip()


def label(SCREEN, text, fontsize, x, y, WIDTH, height):
    font = pygame.font.SysFont("comicsansms", fontsize)
    text = font.render(text, True, GREY)
    box = text.get_rect()
    box.center = (x // 2, y // 2)
    SCREEN.blit(text, box)


def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()

        SCREEN.fill(WHITE)
        label(SCREEN, "TIC TAC TOE", 40, 300, 250, 20, 20)
        button(SCREEN, "Play", 150, 650, 20, 20, BLUE, main)
        button(SCREEN, "Quit", 450, 650, 20, 20, RED, game_exit)
        pygame.display.flip()


if __name__ == "__main__":

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREY = (84, 83, 82)

    SCREEN_SIZE = (300, 380)
    DRAWING_SIZE = (50, 50)
    HEIGHT = 93
    WIDTH = 93

    MARGIN = 5
    TOKEN_margin = 15
    COLOR = WHITE
    TEXT  = "TIC TAC TOE"

    pygame.init()
    SCREEN = display_window()
    menu()

# this class will be responsible for handling user input and displaying the game state object

from tkinter import W, Widget
import pygame
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
FPS = 15
IMAGES = {}

#  Initialize a global dictionary of the images
def load_images():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bP', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load('images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))

# This will be the main driver for the code: handle user input and update the graphics
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color('white'))
    gs = ChessEngine.GameState()
    load_images()
    draw_game_state(screen, gs)
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        
        clock.tick(FPS)
        pygame.display.flip()
 
# draws graphics for current game state 
def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)    
    

# draw the squares on the board (top left square is always light)
def draw_board(screen):
    colors = [pygame.Color('white'), pygame.Color('gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    
# draws the pieces on the board using the current game state
def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--':
                screen.blit(IMAGES[piece], pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
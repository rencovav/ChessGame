# handling user input, displaying the current GameState object

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def load_images():
    pieces = ["bB", "bK", "bN", "bp", "bQ", "bR", "wB", "wK", "wN", "wp", "wQ", "wR"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Chess/images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()  # creating a game state object
    load_images()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)

def draw_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row+column)%2)]
            p.draw.rect(screen, color, p.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, board):
    pass



if __name__ == "__main__":
    main()

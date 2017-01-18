import pygame
import time

class Player:
    """
    Class player manages the players infomation
    about the on going game. This includes which
    piece the player is and where their piece are
    placed on the game board
    """
    def __init__(self,name,color):
        self.name = name
        self.color = color
        self.piece_loc = []
    def add_piece(self,piece):
        """
        Tracks the location of where the player has
        placed their piece on the board
        """
        self.piece_loc.append(piece)


class Board:
    """
    Class Board handles calculating where x's
    and o's whereplaced in the GUI. It also
    calculates if a player has won the game
    or not
    """
    def __init__(self):
        self.win_states = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
            [1,4,7],
            [2,5,8],
            [3,6,9],
            [1,5,9],
            [3,5,7]
        ]
        self.avalible_move = {1,2,3,4,5,6,7,8,9}
        self.click_map = [
            (150,150),
            (250,150),
            (350,150),
            (150,250),
            (250,250),
            (350,250),
            (150,350),
            (250,350),
            (350,350)
        ]
        self.turn_count = 0


    def check_win(self,p_loc):
        """
        Checks to see if a player owns the pieces
        that make up one of the possible win states
        """
        for states in self.win_states:
            result = [loc for loc in p_loc if loc in states]
            if len(result) == 3:
                return True
        return False


    def calc_space(self,x,y):
        """
        Calculates which square the player wants to
        place their piece depending on where their
        mouse was clicked
        """
        space = 0
        if 100 < x < 200 and 100 < y < 200:
            space = 1
        elif 200 < x < 300 and 100 < y < 200:
            space = 2
        elif 300 < x < 400 and 100 < y < 200:
            space = 3
        elif 100 < x < 200 and 200 < y < 300:
            space = 4
        elif 200 < x < 300 and 200 < y < 300:
            space = 5
        elif 300 < x < 400 and 200 < y < 300:
            space = 6
        elif 100 < x < 200 and 300 < y < 400:
            space = 7
        elif 200 < x < 300 and 300 < y < 400:
            space = 8
        elif 300 < x < 400 and 300 < y < 400:
            space = 9

        # removes the space from avalible moves
        if space in self.avalible_move and space != 0:
            self.avalible_move.remove(space)
            return space
        else:
            return space


def Start():

    # Initilizing game definitions
    size = [500, 600]
    white = 255, 255, 255
    black = 0, 0, 0
    blue = 0, 0, 255
    red = 255, 0, 0
    green = 0, 255, 0
    left = 1

    pygame.init()
    pygame.font.init()
    title_font = pygame.font.SysFont("monospace", 20)
    ply_font = pygame.font.SysFont("monospace", 15)
    pygame.display.set_caption("Tic Tac Toe")
    screen = pygame.display.set_mode(size)


    # Defining Player and the Gameboard
    Player1 = Player("Player 1", red)
    Player2 = Player("Player 2", blue)
    game_board = Board()
    player_que = [Player1,Player2]

    # Player 1 will always go first
    player_turn = 0

    # render text
    title = title_font.render("Tic Tac Toe",True, blue)
    ply_1 = ply_font.render(Player1.name,True, red)
    ply_2 = ply_font.render(Player2.name,True, blue)
    done = False
    win = False
    # Drawing game board
    screen.fill(white)
    screen.blit(title, (182, 30))
    screen.blit(ply_1, (50, 450))
    screen.blit(ply_2, (380, 450))

    # Vertical lines
    pygame.draw.line(screen, black, [100, 100], [100,400], 5)
    pygame.draw.line(screen, black, [200, 100], [200,400], 5)
    pygame.draw.line(screen, black, [300, 100], [300,400], 5)
    pygame.draw.line(screen, black, [400, 100], [400,400], 5)
    # Horizontal lines
    pygame.draw.line(screen, black, [100, 100], [400,100], 5)
    pygame.draw.line(screen, black, [100, 200], [400,200], 5)
    pygame.draw.line(screen, black, [100, 300], [400,300], 5)
    pygame.draw.line(screen, black, [100, 400], [400,400], 5)


    while not done:
        for event in pygame.event.get():
            player_move = player_que[player_turn]
            # mouse click event
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == left:
                x, y = event.pos
                space = game_board.calc_space(x,y)
                if space != 0:
                    # place player piece on the game board
                    player_que[player_turn].add_piece(space)
                    color = player_que[player_turn].color
                    loc = game_board.click_map[space-1]
                    pygame.draw.circle(screen,color,loc,25,0)
                    # checks for a win
                    if 9 >= game_board.turn_count >= 4:
                        win = game_board.check_win(player_move.piece_loc)
                        if win == True:
                            outtxt = player_que[player_turn].name + " has won!"
                            out = title_font.render(outtxt,True, black)
                            done = True
                    # change players turn update piece
                    if player_turn == 0:
                        player_turn = 1
                        ply_2 = ply_font.render(Player2.name,True, black)
                        ply_1 = ply_font.render(Player1.name,True, red)
                        pygame.display.update()

                    elif player_turn == 1:
                        player_turn = 0
                        ply_1 = ply_font.render(Player1.name,True, black)
                        ply_2 = ply_font.render(Player2.name,True, blue)
                        pygame.display.update()
                    game_board.turn_count = game_board.turn_count + 1
                    if game_board.turn_count == 9 and win == False:
                        out = title_font.render("Cats game!",True, black)
                        done = True
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            pygame.display.flip()
    screen.blit(out, (145, 500))
    pygame.display.flip()
    time.sleep(5)

if __name__ == "__main__":
    Start()

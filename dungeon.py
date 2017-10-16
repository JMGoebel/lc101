import subprocess as sp
import msvcrt

class Dungeon():
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.showAll = True
        self.isOver = False
        self.player_X = 5
        self.player_Y = 5
        self.player_hp = 100
        self.player_att = 1
        self.player_def = 1
        self.grid = self.createMap()

    def drawMap(self):
        row = ""
        self.grid[(self.player_X, self.player_Y)] = "@"
        for x in range(self.length):
            for y in range(self.width):
                row += self.grid[(x ,y)]
            print(row)
            row = ""
        print("H: {} A: {} D: {}".format(self.player_hp, self.player_att, self.player_def))

    def createMap(self):
        grid = {}
        for x in range(self.length):
            for y in range(self.width):
                if x == 0 or x == self.length - 1 or y == self.width -1 or y == 0:
                    grid[(x, y)] = "#"
                else:
                    grid[(x, y)] = '.'
        return grid
    
    def isWall(self, x, y):
        return game.grid[(self.player_X + x, self.player_Y + y)] == "#"

tmp = sp.call('cls',shell=True)

def move():
    cmd = msvcrt.getch().decode('ASCII')
    if cmd == 's':
        if game.isWall(1, 0):
            return
        game.grid[(game.player_X, game.player_Y)] = '.'
        game.player_X += 1
        return
    elif cmd == 'w':
        if game.isWall(-1, 0):
            return
        game.grid[(game.player_X, game.player_Y)] = '.'
        game.player_X -= 1
        return
    elif cmd == 'd':
        if game.isWall(0, 1):
            return
        game.grid[(game.player_X, game.player_Y)] = '.'
        game.player_Y += 1
        return
    elif cmd == 'a':
        if game.isWall(0, -1):
            return
        game.grid[(game.player_X, game.player_Y)] = '.'
        game.player_Y -= 1
        return
    elif cmd == '0':
        game.isOver = True

def game_loop(game):
    # clear screen
    sp.call('cls',shell=True)
    #draw map
    game.drawMap()
    #draw player
    #get input
    move()
    #test conditions
    #loop

game = Dungeon("test",10,50)

while not game.isOver:
    game_loop(game)

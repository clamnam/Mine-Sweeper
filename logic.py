import numpy as np
import random 

class logic:
    def __init__(self,level):

        self.grid_array = []
        self.level = level
        self.difficulty = {"easy":(10,10,10),"intermediate":(16,16,10),"hard":(16,30,99)}
        if self.level in self.difficulty:
            self.cols = self.difficulty[self.level][0]
            self.rows = self.difficulty[self.level][1]

    def mask_grid(self):
        if self.level in self.difficulty:
            # creates empty grid
            self.cols = self.difficulty[self.level][0]
            self.rows = self.difficulty[self.level][1]
            matrix = [['o' for _ in range(self.cols)] for _ in range(self.rows)]

            for x,row in enumerate(matrix) :print(matrix[x])


    def grid(self):
        # dictionary to with difficulty information


            matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
            
            self.mines(self.difficulty[self.level][2],self.cols,self.rows)
            return "invalid difficulty entry"
    
    def mines(self,mines,cols,rows):
        mine_coords = []
        # create mine coords
        for mine in range(mines):
            x = random.randrange(rows)
            y = random.randrange(cols)
            mine_coords.append((x,y))
        # enter mines in grid
        for mines in mine_coords:
            self.grid_array[mines[0]][mines[1]] = 9
            self.hinting(mines[0],mines[1])

        print(self.grid_array)



    def hinting(self,coord_x,coord_y):
        def add_hint(x,y):
            if 0 <= x < len(self.grid_array) and 0 <= y < len(self.grid_array) :
                self.grid_array[x][y]+=1
        # following x
        add_hint(coord_x+1,coord_y)
        # previous x
        add_hint(coord_x-1,coord_y)
        # following y
        add_hint(coord_x,coord_y+1)
        # previous y
        add_hint(coord_x,coord_y-1)
        # previous x,y
        add_hint(coord_x-1,coord_y-1)
        # following x,y
        add_hint(coord_x+1,coord_y+1)
        # previous x following y
        add_hint(coord_x-1,coord_y+1)
        # previous y following x
        add_hint(coord_x+1,coord_y-1)



        



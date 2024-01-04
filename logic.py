import numpy as np
import random 

class logic:
    def __init__(self,level):

        self.grid_array = []
        self.level = level
    def grid(self):
        # dictionary to with difficulty information
        difficulty = {"easy":(10,10,10),"intermediate":(16,16,10),"hard":(16,30,99)}

        if self.level in difficulty:
            # creates empty grid
            cols = difficulty[self.level][0]
            rows = difficulty[self.level][1]
            self.grid_array=np.zeros((cols,rows))
            
            self.mines(difficulty[self.level][2],cols,rows)
        else:
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
            # self.hinting(mines[0],mines[1])

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



        

sweep = logic('intermediate')

sweep.grid()

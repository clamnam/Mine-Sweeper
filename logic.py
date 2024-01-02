import numpy as np
import random 

class logic:
    def __init__(self,level):

        self.grid_array = []
        self.level = level
    def grid(self):
        # dictionary to with difficulty information
        difficulty = {"easy":(10,10,10),"intermediate":(16,16,40),"hard":(16,30,99)}

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
            mine_coords.append((random.randrange(cols),random.randrange(rows)))
        # enter mines in grid
        for x,mines in enumerate(mine_coords):
            self.grid_array[mines[0]][mines[1]] = ('9')
        print(self.grid_array)


        
    


sweep = logic('intermediate')

sweep.grid()

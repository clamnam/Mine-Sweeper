import numpy as np
import random 

class logic:
    def __init__(self,level):

        self.grid_array = []
        self.level = level
    def grid(self):
        # dictionary to with difficulty information
        difficulty = {"easy":(10,10,10),"intermediate":(16,16,3),"hard":(16,30,99)}

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
            self.grid_array[mines[1]][mines[0]] = (9)
            self.hinting(mines[1],mines[0])

        print(self.grid_array)



    def hinting(self,coord_x,coord_y):
        # pass
        def add_following_x_hint():
            print(coord_x,coord_y)
            self.grid_array[coord_y][coord_x-1]+=1
        # def add_following_y_hint():
        #     self.grid_array[coord_y+1][coord_x]+=1

        # def add_previous_x_hint():
        #     self.grid_array[coord_y-1][coord_x]+=1

        # def add_previous_y_hint():
        #     self.grid_array[coord_y-1][coord_x]+=1
        if(coord_x < len(self.grid_array[coord_y])-1):
            print(coord_y,coord_x,'incase')
            add_following_x_hint()
        # if(coord_x >0):
        #     add_previous_x_hint()
        # if(coord_y+1 < len(self.grid_array[coord_y])):
        #     add_following_y_hint()
        # if(coord_y):
        #     add_previous_y_hint()

        

sweep = logic('intermediate')

sweep.grid()

import random


class logic:
    def __init__(self, level):
        self.grid_array = []

        self.grid_array = []
        self.level = level
        self.difficulty = {
            "easy": (10, 10, 10),
            "intermediate": (16, 16, 10),
            "hard": (16, 30, 99),
        }
        if self.level in self.difficulty:
            self.cols = self.difficulty[self.level][0]
            self.rows = self.difficulty[self.level][1]
            self.mine_count = self.difficulty[self.level][2]
            self.matrix = [["o" for _ in range(self.cols)] for _ in range(self.rows)]

    def mask_grid(self):
        return self.matrix

    def grid(self):
        # dictionary to with difficulty information
        self.grid_array = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.mines(self.mine_count, self.cols, self.rows)
        return self.grid_array

    def mines(self, mines, cols, rows):
        mine_coords = []
        # create mine coords
        for mine in range(mines):
            x = random.randrange(rows)
            y = random.randrange(cols)
            mine_coords.append((x, y))
        # enter mines in grid
        for mines in mine_coords:
            self.grid_array[mines[0]][mines[1]] = 9
            self.hinting(mines[0], mines[1])

    def hinting(self, coord_x, coord_y):
        def add_hint(x, y):
            if 0 <= x < len(self.grid_array) and 0 <= y < len(self.grid_array[0]):
                self.grid_array[x][y] += 1

        # following x
        add_hint(coord_x + 1, coord_y)
        # previous x
        add_hint(coord_x - 1, coord_y)
        # following y
        add_hint(coord_x, coord_y + 1)
        # previous y
        add_hint(coord_x, coord_y - 1)
        # previous x,y
        add_hint(coord_x - 1, coord_y - 1)
        # following x,y
        add_hint(coord_x + 1, coord_y + 1)
        # previous x following y
        add_hint(coord_x - 1, coord_y + 1)
        # previous y following x
        add_hint(coord_x + 1, coord_y - 1)

    def main(self):
        data = (self.grid(), self.mask_grid())
        return data
